from django.urls import path
from .views import *

app_name = 'chats'

urlpatterns = [
    path('', ChatList.as_view(), name='chat-list'),
    path('<int:pk>/', ChatDetail.as_view(), name='chat-detail'),
    path('comments/<int:pk>/update', UpdateComment.as_view(), name='update-comment'),
    path('comments/<int:pk>/delete', DeleteComment.as_view(), name='delete-comment')
]
