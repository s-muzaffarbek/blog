from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from .views import SignUpView, LoginBlogView, UserEditView, MyUserView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='signup'),
    path('login', LoginBlogView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('user/<int:pk>', MyUserView.as_view(), name='user_profile'),
    path('edit/<int:pk>', UserEditView.as_view(), name='user_edit'),
    path(
        'change-password/', PasswordChangeView.as_view(
            template_name='registration/change_password.html',
            success_url='/registration/change-password-done'
        ), name='change_password'),
    path('change-password-done/', PasswordChangeDoneView.as_view(
            template_name='registration/change_password_done.html'
            ), name='change_password_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]