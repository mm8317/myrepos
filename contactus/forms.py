from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=300,widget=forms.TextInput(attrs={'placeholder':'Please enter your username'}))
    email =  forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Please enter your email address'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Please enter firstname'}))
    last_name =  forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Please enter lastname'}))
    password_1 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'Please enter password'}))
    password_2 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'Please re-enter password'}))

    def clean_username(self):
        user = self.cleaned_data['username']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('username already exist')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email already exist')
        else:
            return email
    def clean_password_2(self):
        password1 = self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 != password2:
            raise forms.ValidationError('passwords do not match')
        elif len(password2)<8:
            raise forms.ValidationError('password is to short')
        elif not any(i.isupper() for i in password2):
            raise forms.ValidationError('password must contain at least one uppercase letter')
        else:
            return password1


class LoginForm(forms.Form):
        user = forms.CharField(max_length=50)
        password = forms.CharField(max_length=50)

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())