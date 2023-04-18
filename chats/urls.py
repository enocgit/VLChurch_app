from django.urls import path
from .views import *

app_name = 'chats'

urlpatterns = [
    # path('', ChatList.as_view(), name='chat-list'),
    path('<int:pk>/', ChatDetail.as_view(), name='chat-detail'),
]
