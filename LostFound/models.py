from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    ITEM_TYPES = [
        ('card', 'Card'),
        ('keys', 'Keys'),
        ('purse', 'Purse'),
        ('mobile', 'Mobile'),
        ('watch', 'Watch'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES)
    other_type = models.CharField(max_length=100,null=True)
    date_time = models.DateTimeField(auto_now_add=True,blank = True)
    is_recovered = models.BooleanField(default=False)
    recovered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='recovered_items')
    media = models.FileField(upload_to='item_media/', blank=True, null=True)
