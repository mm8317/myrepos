import http

from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserRegisterForm,LoginForm,ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def contactus(request):
    return render(request, 'contactus/contactus_page.html')

def user_register(request):
    if request.method == 'POST':
        form_register = UserRegisterForm(request.POST)
        if form_register.is_valid():
            data = form_register.cleaned_data
            # User.objects.create_user(username=data['username']
            # email = data['email'], first_name=data['first_name'], last_name=data['last_name'],
                                     # password=data['password_1'])
            return redirect('home:home-func')
    else:
        form_register = UserRegisterForm()
        context = {'form_register': form_register}
        return render(request, 'contactus/user_register.html', context)
    # return render(request, 'contactus/user_register.html')

def user_login(request):
    if request.method == 'POST':
        form_login = LoginForm(request.POST)
        if form_login.is_valid():
            data = form_login.cleaned_data
            user = authenticate(request, username=data['user'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('home:home-func')


    else:
        form_login = LoginForm()
    return render(request,'contactus/login.html',{'form_login': form_login})

def user_logout(request):
    logout(request)
    return redirect('home:home-func')

@login_required()
def change_password(request):
    if request.method == 'POST':
        user = request.user
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            old_password = data['old_password']
            new_password1 = data['new_password1']
            new_password2 = data['new_password2']
            # if old_password != user.password:
            if not user.check_password(old_password):
                return HttpResponse('your old password does not match')
            elif new_password1 != new_password2:
                return HttpResponse('your new password does not match')
            else:
                user.set_password(new_password2)
                user.save()
                return HttpResponse('password changed successfully')

    else:
        form = PasswordChangeForm()
    return render(request,'contactus/changepassword.html',{'form':form})