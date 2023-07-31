from django.shortcuts import redirect, render
from django.contrib import messages
from incidentreporting.forms import IncidentForm
from .models import Incident
from django.db.models import Q
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Point
from django.contrib.auth.decorators import login_required

@login_required
def report_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save(commit=False)
            if incident.incident_type == 'other':
                incident.incident_type = 'Other'
            incident.user = request.user
            latitude = float(request.POST.get('latitude'))
            longitude = float(request.POST.get('longitude'))
            print(latitude)
            print(longitude)
            incident.location = Point(longitude, latitude)
            incident.save()
            form.save_m2m()
            messages.success(request, 'Incident reported successfully!')
            return redirect('users-home')
    else:
        form = IncidentForm()
    return render(request, 'incidentreporting/incidentreporting.html', {'form': form})



@login_required
def view_incident(request):
    # Get all incidents ordered by date and time
    incidents = Incident.objects.order_by('-registered_time')
    # Searching incidents based on a query parameter
    search_query = request.GET.get('search')
    if search_query:
        incidents = incidents.filter(
            Q(incident_type__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    return render(request, 'incidentreporting/view_incident.html', {'incidents': incidents})

