from django.shortcuts import render
from django.views.generic import View, ListView
from chat.models import Chat

class ChatList(ListView):
    model = Chat
    template_name = 'chat/chat_list.html'
    context_object_name = 'chats'
    
    
    # model = 
    # def get_context_data(self):
    #     context = super().get_context_data(self)
    #     context['chats'] = Chat.objects.all()
    #     return context
    
