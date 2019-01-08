from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_object_or_404
from . import views


app_name = 'coreApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('mark_notifications_as_read', views.mark_notifications_as_read, name='mark_notifications_as_read'),

    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='coreApp/password_change.html',
        success_url=reverse_lazy('coreApp:password_change_done'),
    ), name='password_change'),

    path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='coreApp/password_change_done.html',
    ), name='password_change_done'),

    path('reset-password/', auth_views.PasswordResetView.as_view(
        template_name='coreApp/forgot_password.html',
        email_template_name='coreApp/password_reset_email.html',
        subject_template_name='coreApp/password_reset_subject.txt',
        success_url=reverse_lazy('coreApp:password_reset_done')
    ), name='password_reset'),

    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='coreApp/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='coreApp/password_reset_confirm.html',
        success_url=reverse_lazy('coreApp:password_reset_complete')

    ), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='coreApp/password_reset_complete.html',
    ), name='password_reset_complete')
]
