from django.shortcuts import render, redirect
from django.http import HttpResponse
from members.models import *

# User Registration imports.
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Error messages #
from django.contrib import messages

# Auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# custom decorator
from .decorators import unauthenticated_user, allowed_users



# custom decorator
@unauthenticated_user
# Register
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='member')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


# custom decorator
@unauthenticated_user
# Login
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # return redirect('my-profile')
            # return redirect('member-homepage')
            return redirect('add-id-number')

        else:
            messages.info(request, 'Username OR Password is incorrect!')

    context = {}
    return render(request, 'accounts/login.html', context)


# Logout
def logoutUser(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
# # custom decorator
# @allowed_users(allowed_roles=['clinic'])
# def AdminPage(request):
#     context = {}
#     return render(request, 'accounts/admin.html', context)