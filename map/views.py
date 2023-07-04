from django.shortcuts import render
from incidentreporting.models import Incident
from django.core import serializers
import json



def map_view(request):
    # Fetch incidents data from your model or database
    incidents = Incident.objects.all()
    incidents_data = [{'latitude': incident.location.y, 'longitude': incident.location.x} for incident in incidents]
    
    context = {
        'incidents': json.dumps(incidents_data)  # Serialize incidents_data as JSON
    }
    return render(request, 'map/map.html', context)