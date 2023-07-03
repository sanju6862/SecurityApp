from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Incident(models.Model):
    INCIDENT_TYPES = [
        ('theft', 'Theft'),
        ('harassment', 'Harassment'),
        ('vandalism', 'Vandalism'),
        ('other', 'Other'),  # Add an "other" option
    ]
    ZONES = [
        ('near LC','Near LC'),
        ('near gymkhana','Near Gymkhana'),
        ('near rajputana','Near Rajputana'),
        ('near newgirls hostel','Near Newgirls Hostel')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPES)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    location = models.PointField()
    zone = models.CharField(max_length=100, choices=ZONES)
    description = models.TextField()
    media_file = models.FileField(upload_to='incident_media/', blank=True, null=True)
    registered_time = models.DateTimeField(auto_now_add=True)
