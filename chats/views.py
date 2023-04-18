from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView, DetailView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from chats.models import Chat, Comment
from .forms import CommentForm

# class ChatList(LoginRequiredMixin, ListView):
#     model = Chat
#     template_name = 'chats/chat_list.html'
#     context_object_name = 'chats'

# class ChatDetail(LoginRequiredMixin, DetailView):
#     model = Chat
#     template_name = 'chats/chat_detail.html'
#     # context_object_name = 'chat'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['chat'] = get_object_or_404(Chat, pk=self.kwargs['pk'])
#         # context['chat'] = Chat.objects.get(pk=1)
#         context['chats'] = Chat.objects.all()
        
#         return context
    
# class ChatList(ListView):
#     model = Chat
#     template_name = 'chats/chat_list.html'
#     context_object_name = 'chats'

#     def get(self, request, *args, **kwargs):
#         # Get the chat ID from the cookie
#         chat_id = request.COOKIES.get('chat_id')
        
#         # If a chat ID is stored in the cookie, redirect the user to the detail view of that chat
#         if chat_id:
#             return redirect(reverse('chats:chat-detail', kwargs={'pk': chat_id}))

#         # Otherwise, display the chat list as usual
#         return super().get(request, *args, **kwargs)

class ChatDetail(FormView):
    # fields = ('message')
    form_class = CommentForm
    model = Chat
    template_name = 'chats/chat_detail.html'
    
    def get(self, request, *args, **kwargs):
        # Store the chat ID in a cookie
        response = super().get(request, *args, **kwargs)
        response.set_cookie('chat_id', self.kwargs['pk'])
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chat'] = get_object_or_404(Chat, pk=self.kwargs['pk'])
        context['chats'] = Chat.objects.all()
        
        return context
    
    def post(self, request, *args, **kwargs):
        # super().post(*args, **kwargs)
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.user = self.request.user
            comment.chat = get_object_or_404(Chat, pk=self.kwargs['pk'])
            comment.save()

            return redirect('chats:chat-list')
        return self.form_invalid(form)

    
