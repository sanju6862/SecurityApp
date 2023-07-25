from django.shortcuts import render
from .models import UserProfile, Message
from django.contrib.auth.models import User
from django.db.models import Q

def chat_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'chat/chat_list.html', {'profiles': profiles})


def chat_detail(request, user_id):
    # Retrieve the messages for the given user_id or any other relevant logic
    messages = Message.objects.filter(Q(sender_id=user_id) | Q(receiver_id=user_id))  # Adjust the filtering logic as per your requirements
    context = {
        'messages': messages,
        'user_id': user_id,
    }
    return render(request, 'chat/chat_details.html', context)

def send_message(request):
    if request.method == 'POST':
        sender = request.user
        receiver_id = request.POST['receiver_id']
        message_content = request.POST['message']

        receiver = User.objects.get(id=receiver_id)

        # Create a new message instance
        message = Message.objects.create(sender=sender, receiver=receiver, message=message_content)

        return redirect('chat/chat_details', user_id=receiver_id)

    return render(request, 'chat/send.html')

def reply_message(request, message_id):
    if request.method == 'POST':
        sender = request.user
        parent_message = Message.objects.get(id=message_id)
        receiver = parent_message.sender  # Reply to the original sender
        message_content = request.POST['message']

        # Create a new message instance as a reply
        message = Message.objects.create(sender=sender, receiver=receiver, message=message_content)

        return redirect('chat_detail', user_id=receiver.id)

    return render(request, 'chat/reply.html', {'message_id': message_id})