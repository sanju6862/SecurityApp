from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# from .models import Location

@csrf_exempt
def location_sender(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        print(latitude)
        print(longitude)
        # Implement the logic to handle the panic alert
        # Notify the control room, emergency services, etc.

        # Store the panic button press in the database if required
        # location = Location(latitude=latitude, longitude=longitude)
        # location.save()

        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error'})
def panic_button(request):
    return render(request,'panic_button/location_sender.html')