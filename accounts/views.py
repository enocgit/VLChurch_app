from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

class Login(LoginView):
    model = get_user_model()
    template_name = 'accounts/login.html'
    fields = '__all__'
    # success_url = reverse_lazy('chats:chat-list')
    
    def get_success_url(self):
        # return redirect('chats:chat-detail')
        return reverse_lazy('chats:chat-detail', kwargs={'pk': 1})