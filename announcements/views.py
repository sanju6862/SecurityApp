from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnnouncementForm
from .models import Announcement
from django.contrib import messages

def announcement_list(request):
    announcements = Announcement.objects.order_by('-timestamp')
    return render(request, 'announcements/announcement_list.html', {'announcements': announcements})

def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.author = request.user
            announcement.save()
            messages.success(request, 'Announcement is created successfully!')
            return redirect('users-home')
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/create_announcement.html', {'form': form})

def update_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)

    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcements')
    else:
        form = AnnouncementForm(instance=announcement)

    return render(request, 'announcements/update_announcement.html', {'form': form, 'announcement': announcement})

def delete_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)
    announcement.delete()
    return redirect('announcements')