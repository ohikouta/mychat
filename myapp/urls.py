from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_chat_message, name='create_chat_message'),
    path('chat/messages/', views.chat_message_list, name='chat_message_list'),
    # path('hello/', views.hello_world, name='hello_world'),
]