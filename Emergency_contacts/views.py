# views.py
from django.shortcuts import render
from .models import EmergencyContact

def Emergency_contacts(request):
    emergency_contacts = EmergencyContact.objects.all()
    return render(request, 'Emergency_contacts/Emergency_contacts.html', {'emergency_contacts': emergency_contacts})
