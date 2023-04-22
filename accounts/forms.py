from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from members.models import Member

class LoginForm(AuthenticationForm):
    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'p-20', }),
            'password': forms.PasswordInput(attrs={'class': 'p-20'}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'mb-8', 'placeholder': 'old password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'mb-8', 'placeholder': 'new password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'mb-8', 'placeholder': 'confirm new password'}))

    class Meta:
        model = Member
        fields = ['old_password', 'new_password1', 'new_password2']