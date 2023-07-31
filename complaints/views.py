from django.shortcuts import get_object_or_404, render,redirect
from securityApp import settings
from complaints.forms import ComplaintForm
from django.contrib import messages
from complaints.models import *
from django.core.mail import send_mail
from notifications.models import Notification
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def create_complaint(request):  # sourcery skip: extract-method
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user  # Assign the current user
            complaint.save()
            # subject = "Complaint"
            # message = "Complaint registered"
            # from_email = settings.EMAIL_HOST_USER
            # recipient_list = ["ishwarkumawat68622@gmail.com"]
            # send_mail(subject,message,from_email,recipient_list)
            user_email = complaint.user.email
            email_subject = 'Complaint Status Update'
            email_message = f"Your complaint is registered successfully. \n\nComplaint Subject: {complaint.subject} \n\nComplaint Subject: {complaint.description}"
            send_mail(email_subject, email_message, 'ishwarkumawat686222@gmail.com', [user_email], fail_silently=False)
            messages.success(request, 'Your complaint is registered successfully.')
            return redirect('/')  # Redirect to the complaints list page
    else:
        form = ComplaintForm()
    return render(request, 'complaints/complaints.html', {'form': form})

@login_required
def view_complaints(request):
    user = request.user
    search = request.GET.get('search', '')
    
    if user.profile.user_type == "security":
        complaints = Complaint.objects.order_by('-created_at')
        if search:
            complaints = complaints.filter(
                Q(subject__icontains=search) |
                Q(description__icontains=search)
            )
    elif user.profile.user_type in ["student", "faculty"]:
        complaints = Complaint.objects.filter(user=user)
        if search:
            complaints = complaints.filter(
                Q(subject__icontains=search) |
                Q(description__icontains=search)
            )

    return render(request, 'complaints/view_complaints.html', {'complaints': complaints, 'search': search})


@login_required
def update_complaint_status(request):
    if request.method == 'POST':
        complaint_id = request.POST.get('complaint_id')
        status = request.POST.get('status-selector')
        remarks = request.POST.get('remarks')

        if complaint_id and status:
            complaint = get_object_or_404(Complaint, pk=complaint_id)
            # previous_status = complaint.status  # Store the previous status
            complaint.status = status
            complaint.Remarks = remarks
            complaint.save()
         # # Send email notification to the user
            user_email = complaint.user.email
            email_subject = 'Complaint Status Update'
            email_message = f"Your complaint is now under status '{status}'.\n\nRemarks: {remarks}"
            send_mail(email_subject, email_message, 'ishwarkumawat686222@gmail.com', [user_email], fail_silently=False)
            notification = Notification(user=complaint.user, message=email_message)
            notification.save()
            # send_mail(
            #     'Testing',
            #     'Here is the message.',
            #     'ishwarkumawat686222@gmail.com',
            #     ['ishwarkumawat68622@gmail.com'],
            #     fail_silently=False,
            # )

        else:
            messages.success(request, 'Invalid complaint ID or missing status')


        return redirect('view_complaints')  # Redirect to the view_complaints URL name
