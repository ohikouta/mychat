from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ChatMessage
from .forms import ChatMessageForm

# def hello_world(request):
#     return HttpResponse("Hello, World!")

# chat
def create_chat_message(request):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat_message_list')
    else:
        form = ChatMessageForm()
    return render(request, 'chat/create_chat_message.html', {'form': form})


def chat_message_list(request):
    chat_messages = ChatMessage.objects.all()
    return render(request, 'chat/chat_message_list.html', {'chat_messages': chat_messages})

