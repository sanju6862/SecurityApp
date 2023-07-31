from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notifications.models import Notification

@login_required
def notification_view(request):
    if request.method == 'GET':
        # Retrieve the user's notifications
        user_notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')[:5]

        # Render the HTML template
        return render(request, 'notifications/notifications.html', {'notifications': user_notifications})

    elif request.method == 'POST':
        # Retrieve the user's notifications
        user_notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')[:10]

        # Prepare the JSON response
        notifications = [{'message': notification.message} for notification in user_notifications]

        # Return the JSON response
        return JsonResponse(notifications, safe=False)
