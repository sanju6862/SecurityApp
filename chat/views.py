# chat/views.py
from django.http import JsonResponse
from django.shortcuts import render
from .models import Message
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q


def chat(request, id1, id2):
    user1 = get_object_or_404(User, pk=id1)
    user2 = get_object_or_404(User, pk=id2)
    
    # Use Q object to perform OR operation on the sender and receiver fields
    messages = Message.objects.filter(
        (Q(sender=user1) & Q(receiver=user2)) |
        (Q(sender=user2) & Q(receiver=user1))
    ).order_by('timestamp')

    return render(request, 'chat/chat.html', {
        'user1': user1,
        'user2': user2,
        'messages': messages,
    })


def send_message(request, id1, id2):
    user1 = get_object_or_404(User, pk=id1)
    user2 = get_object_or_404(User, pk=id2)
    if request.method == 'POST':
        content = request.POST.get('message')
        if content:
            Message.objects.create(sender=user1, receiver=user2, content=content)
    return chat(request,id1,id2)
