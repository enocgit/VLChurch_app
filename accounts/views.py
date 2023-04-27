from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
# from django.contrib.messages.views import 
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import LoginForm
from .forms import CustomPasswordChangeForm
from chats.models import Chat

class Login(LoginView):
    model = get_user_model()
    template_name = 'accounts/login.html'
    # fields = '__all__'
    form_class = LoginForm
    # authentication_form = LoginForm
    
    # success_url = reverse_lazy('chats:chat-list')
    
    def get_success_url(self):
        # return redirect('chats:chat-detail')
        chat_id = self.request.COOKIES.get('chat_id')
        if chat_id:
            return reverse_lazy('chats:chat-detail', kwargs={'pk': chat_id})
        else:
            general_chat_id = Chat.objects.get(name="General").pk
            return reverse_lazy('chats:chat-detail', kwargs={'pk': general_chat_id})
        
    def form_invalid(self, form):
        messages.error(self.request, 'Username or password is incorrect.', extra_tags='login-error')
        return redirect(reverse('accounts:login'))


class PasswordChange(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:password-change-done')
    form_class = CustomPasswordChangeForm

    def form_invalid(self, form):
        messages.error(self.request, "The passwords don't match.")
        return redirect(reverse('accounts:password-change'))

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'

    # def password_sucess(request):
    #     return render(request, 'accounts/password_change_done.html')