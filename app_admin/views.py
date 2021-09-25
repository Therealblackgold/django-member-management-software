from django.shortcuts import render
from .models import Payment
from members.models import MembershipNumber, Member, Spouse, Family
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UpdateMemberForm, UpdatePendingMemberForm, SpouseForm, FamilyMemberForm
# Admin Authentication Stuff
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
# inlineformset_factory helps create Multiple forms in one form
from .filters import MemberFlilter, Member_id_no
from django.contrib import messages

# Pagination stuff
from django.core.paginator import Paginator

####------------------------------------------- MEMBER VIEWS ------------------------------------####

# Member Detail View
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['Admin'])
# def MemberDetail(request, pk):
#     # member = get_object_or_404(Member, pk=member_id)
#     member = Member.objects.get(id=pk)
#     context = {
#         'member': member,
#     }
#     return render(request, 'christian_admin/member_detail.html', context)


# Admin List Members
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def showprofile(request):
    details = Member.objects.all().order_by('-created')
    identity = MembershipNumber.objects.all()

    # Filter
    myFilter = MemberFlilter(request.GET, queryset=details)
    details = myFilter.qs

    # Pagination
    # p = Paginator(Member.objects.all().order_by('-created'), 5)
    # Pagination with Search Filter
    p = Paginator(myFilter.qs, 5)
    page = request.GET.get('page')
    members = p.get_page(page)

    context = {
        'data': details,
        'myFilter': myFilter,
        'identity': identity,
        'members': members
    }
    return render(request, 'christian_admin/members/ShowProfile.html', context)


# Admin Members Detail View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def showprofiledetails(request, profile_id):
    display_profile = MembershipNumber.objects.get(id=profile_id)
    member = Member.objects.get(id=profile_id)

    return render(request, 'christian_admin/members/ShowProfileDetails.html', {
        'display': display_profile,
        'member': member
    })


# Admin Update Member
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def UpdateMemberAdmin(request, profile_id):

    # Getting data from the form id=pk ,instance=form
    member = Member.objects.get(id=profile_id)
    identity = MembershipNumber.objects.get(id=profile_id)
    # member = Member.objects.get(id=slug_id)
    form = UpdateMemberForm(instance=member)

    # Saving updated form to database
    if request.method == 'POST':
        #print('Printing:', request.POST)
        form = UpdateMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('showprofile')

    context = {'form': form, 'member': member, 'identity': identity}
    return render(request, 'christian_admin/members//update_member.html',
                  context)


# Admin Member Search
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def search_member(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        # membership_no = foregnkey field + id_number = foregnkey value
        members = MembershipNumber.objects.filter(id_number__contains=searched)

        context = {'searched': searched, 'members': members}

        return render(request, 'christian_admin/members/results.html', context)
    else:
        context = {}
        return render(request, 'christian_admin/members/results.html', context)


# Admin Member Payments
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def payments(request, slug_id):
    display = MembershipNumber.objects.get(slug=slug_id)

    context = {'display': display}

    return render(request, 'christian_admin/members/payments.html', context)


# Admin Member Burials
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def burials(request, slug_id):
    display = MembershipNumber.objects.filter(slug=slug_id)
    spouse_display = Spouse.objects.filter(slug=slug_id)
    family_display = Family.objects.filter(slug=slug_id)

    context = {
        'display': display,
        'spouse_display': spouse_display,
        'family_display': family_display
    }

    return render(request, 'christian_admin/members/burials.html', context)


# Admin List Member Burials
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def allburials(request):
    x_member = Member.objects.filter(status='deceased').order_by('-created')
    x_spouse = Spouse.objects.filter(status='deceased').order_by('-created')
    x_family = Family.objects.filter(status='deceased').order_by('-created')
    context = {
        'x_member': x_member,
        'x_spouse': x_spouse,
        'x_family': x_family
    }

    return render(request, 'christian_admin/members/all-burials.html', context)


####------------------------------------------- PENDING MEMBER VIEWS ------------------------------------####


# Admin Update Pending Member
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def UpdatePendingMember(request, pk):

    # Getting data from the form id=pk ,instance=form
    pending = Member.objects.get(status='pending', pk=pk)

    # member = Member.objects.get(id=slug_id)
    form = UpdatePendingMemberForm(instance=pending)

    # Saving updated form to database
    if request.method == 'POST':
        #print('Printing:', request.POST)
        form = UpdatePendingMemberForm(request.POST, instance=pending)
        if form.is_valid():
            form.save()
            return redirect('member-homepage')

    context = {'form': form, 'pending': pending}
    return render(request,
                  'christian_admin/pending-member/pending_member_form.html',
                  context)


# Pending Member Detail View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def PendingMemberDetail(request, pk):
    pending = Member.objects.get(status='pending', pk=pk)
    # identity = MembershipNumber.objects.get(pk=pk)
    # spouse = pending.spousemodel_set.get(user=pending)

    # spouse = pending.spousemodel_set.all()
    context = {
        'pending': pending,
    }
    return render(request,
                  'christian_admin/pending-member/pending-member-view.html',
                  context)


####------------------------------------------- ACTIVE MEMBER VIEWS ------------------------------------####
