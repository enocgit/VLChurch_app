from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'p-20', }),
            'password': forms.PasswordInput(attrs={'class': 'p-20'}),
        }
