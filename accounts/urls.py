from django.urls import path
from .views import *
from django.contrib.auth.views import *


app_name = 'accounts'


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password/change/', PasswordChange.as_view(), name='password-change'),
    path('password/change/done', PasswordChangeDone.as_view(), name='password-change-done'),
    # path('password-reset/', PasswordResetView.as_view(
    #     template_name='accounts/password_reset.html',
    #     success_url='password-reset-done/',
    #     form_class=CustomPasswordResetForm
    # ), name='password_reset'),
    # path('password-reset-done/', PasswordResetDoneView.as_view(
    #     template_name='accounts/password_reset_done.html'
    # ), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    #     template_name='accounts/password_reset_confirm.html'
    # ), name='password_reset_confirm'),
    # path('password-reset-complete/', PasswordResetCompleteView.as_view(
    #     template_name='accounts/password_reset_complete.html'
    # ), name='password_reset_complete'),

]
