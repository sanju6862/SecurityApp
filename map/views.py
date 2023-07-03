from django.shortcuts import render
from incidentreporting.models import Incident
from django.core import serializers
import json


def map_view(request):
    # Fetch incidents data from your model or database
    incidents = Incident.objects.all()
    incidents_data = [{'latitude': incident.location.y, 'longitude': incident.location.x} for incident in incidents]
    incidents_json = json.dumps(incidents_data)

    # Serialize the incidents data to JSON
    # incidents_json = serializers.serialize('json', incidents)

#     incidents_data = json.dumps([
#     {
#         'latitude': incident.location[0],
#         'longitude': incident.location[1],
#     }
#     for incident in incidents
# ])

# Pass the incidents_data to the context or render it to the template
    context = {
        'incidents': incidents_json
    }
    print(incidents[0].location[0])
    print(incidents[0].location[1])
    return render(request, 'map/map.html', context)
