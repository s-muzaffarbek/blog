from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from .forms import SignUpForm, UserEditForm
from .models import MyUser


class MyUserView(View):
    def get(self, request, pk):
        myuser = MyUser.objects.get(pk=pk)
        context = {
            'myuser': myuser,
        }
        return render(request, 'registration/my_user.html', context)


class LoginBlogView(LoginView):
    template_name = 'registration/login.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('blog_list')


class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'


class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'



class UserEditView(UpdateView):
    model = MyUser
    form_class = UserEditForm
    template_name = 'registration/update_user.html'
    success_url = reverse_lazy('blog_list')
