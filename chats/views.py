from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
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
    
class ChatList(ListView):
    model = Chat
    template_name = 'chats/chat_list.html'
    context_object_name = 'chats'

    def get(self, request, *args, **kwargs):
        # Get the chat ID from the cookie
        chat_id = request.COOKIES.get('chat_id')
        
        # If a chat ID is stored in the cookie, redirect the user to the detail view of that chat
        if chat_id:
            return redirect(reverse('chats:chat-detail', kwargs={'pk': chat_id}))

        # Otherwise, display the chat list as usual
        else:
            general_chat_id = Chat.objects.get(name="General").pk
            return redirect(reverse('chats:chat-detail', kwargs={'pk': general_chat_id}))
        # return super().get(request, *args, **kwargs)

class ChatDetail(LoginRequiredMixin, FormView):
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

            return redirect('chats:chat-detail', pk=self.kwargs['pk'])
        return self.form_invalid(form)


class UpdateComment(UpdateView):
    model = Comment
    template_name = 'chats/update-comment.html'
    context_object_name = 'comment'
    fields = ('message',)
    success_url = reverse_lazy('chats:chat-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.editted = True
        form.save()
        return response


class DeleteComment(DeleteView):
    model = Comment
    template_name = 'chats/confirm-comment-delete.html'
    context_object_name = 'comment'
    success_url = reverse_lazy('chats:chat-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_action_url'] = reverse_lazy('chats:delete-comment', self.kwargs['pk'])
        return context