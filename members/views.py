from django.shortcuts import render, redirect
# Models
from .models import Member, Family, Spouse, MembershipNumber
from .forms import MemberForm, IdNumberForm
from django.template.context_processors import csrf
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from website.models import Package
# Error messages
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView
# Pagination stuff
from django.core.paginator import Paginator


# Member homepage + Admin homepage
@login_required(login_url='login')
def memberhomepage(request):
    # Getting request user Member
    user = request.user
    member_no = MembershipNumber.objects.filter(user=user)
    membership_no = MembershipNumber.objects.all()
    member = Member.objects.get(user=user)
    # ------- Admin homepage Views --------- #
    # burials = UpcomingBurials.objects.all()
    burials = Member.objects.filter(status='deceased').last()
    spouse_burials = Spouse.objects.filter(status='deceased').last()
    family_burials = Family.objects.filter(status='deceased').last()
    members = Member.objects.order_by('-created')
    # members count
    members_no = Member.objects.all().count()
    spouse = Spouse.objects.all()
    family = Family.objects.all()
    pending = Member.objects.filter(status='pending').order_by('-created')
    active = Member.objects.filter(status='active')

    # Pending member pagination
    p = Paginator(pending, 2)
    page = request.GET.get('page')
    pending_list = p.get_page(page)

    context = {
        'member': member,
        'member_no': member_no,
        'membership_no': membership_no,
        # ------- Admin homepage Views --------- #
        'members': members,
        'members_no': members_no,
        'pending': pending,
        'active': active,
        'spouse': spouse,
        'family': family,
        'pending_list': pending_list,
        'burials': burials,
        'spouse_burials': spouse_burials,
        'family_burials': family_burials
    }
    return render(request, 'main/homepage.html', context)


# Member profile view (using slug)
@login_required(login_url='login')
def memberprofile(request, slug_id):
    user = request.user
    current_member = Member.objects.get(user=user)
    # xx = Member.objects.get(id=profile_id)
    display = MembershipNumber.objects.get(slug=slug_id)
    context = {'display': display, 'current_member': current_member}
    return render(request, 'members/member.html', context)


# Member Payments
@login_required(login_url='login')
def payments(request, slug_id):
    display = MembershipNumber.objects.get(slug=slug_id)

    context = {'display': display}
    return render(request, 'members/payments.html', context)


# Member Documents View
@login_required(login_url='login')
def memberdocuments(request, slug_id):
    user = request.user
    current_member = Member.objects.get(user=user)
    display = MembershipNumber.objects.get(slug=slug_id)
    context = {'display': display, 'current_member': current_member}
    return render(request, 'members/documents.html', context)


# Member Package View
@login_required(login_url='login')
def memberpackage(request):
    # Getting request user Member
    members = Member.objects.all()
    user = request.user
    member = Member.objects.get(user=user)

    context = {
        'member': member,
        'members': members,
    }
    return render(request, 'members/package.html', context)


# Update member view (with pk)
@login_required(login_url='login')
def updatememberprofile(request, profile_id):
    member = Member.objects.get(id=profile_id)

    if request.method == "POST":
        membershipnumber_form = IdNumberForm(request.POST)
        member_form = MemberForm(request.POST or None,
                                 request.FILES or None,
                                 instance=member)

        # validation check
        if membershipnumber_form.is_valid() and member_form.is_valid():
            membership_no = membershipnumber_form.save()
            member = member_form.save(False)

            # insert thread to post
            member.membership_no = membership_no
            member.save()

            return redirect('member-homepage')

    else:
        membershipnumber_form = IdNumberForm()
        member_form = MemberForm(instance=member)

        args = {}
        args.update(csrf(request))
        args['membershipnumber_form'] = membershipnumber_form
        args['member_form'] = member_form

        return render(request, 'members/update-member.html', args)


# Add Membership number (using id number)
class AddMemberIdNumber(CreateView):
    def get(self, request):
        form = IdNumberForm()
        user = request.user
        membership_id = MembershipNumber.objects.filter(user=user)

        context = {
            'form': form,
            'membership_id': membership_id,
        }

        return render(request, 'members/add_id_number.html', context)

    def post(self, request):
        form = IdNumberForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('id-success')

        context = {'form': form}

        return render(request, 'members/add_id_number.html', context)


# Add membership number success
@login_required(login_url='login')
def idsuccess(request):
    context = {}
    return render(request, 'members/id_success.html', context)


# Update Member Profile
@login_required(login_url='login')
def updatememberprofile(request, profile_id):

    # Getting data from the form id=pk ,instance=form
    member = Member.objects.get(id=profile_id)
    # member = Member.objects.get(id=slug_id)
    form = MemberForm(instance=member)

    # Saving updated form to database
    if request.method == 'POST':
        #print('Printing:', request.POST)
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member-homepage')

    context = {'form': form}
    return render(request, 'members/member-form.html', context)
