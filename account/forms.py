from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'img', 'bio', 'phone', 'birth_day']
