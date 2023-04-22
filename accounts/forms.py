from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from members.models import Member

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': ' focus:border-[#3e535f] focus:ring-[#3e535f] smpp:ml-[-2rem]'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'focus:border-[#3e535f] focus:ring-[#3e535f] smpp:ml-[-2rem]'}))
    class Meta:
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'p-20 border-none ring-[#3e535f]', }),
        #     'password': forms.PasswordInput(attrs={'class': 'p-20 border-none ring-[#3e535f]'}),
        # }
        model = Member

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'focus:border-[#3e535f] focus:ring-[#3e535f]',}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'focus:border-[#3e535f] focus:ring-[#3e535f]',}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'focus:border-[#3e535f] focus:ring-[#3e535f]', }))

    class Meta:
        model = Member
        fields = ['old_password', 'new_password1', 'new_password2']