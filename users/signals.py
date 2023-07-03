import os
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile
import boto3

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    avatar_file = instance.profile.avatar
    s3 = boto3.resource('s3')
    if avatar_file:
        file_name = instance.first_name + ".jpg"
        file =  avatar_file
        object = s3.Object('students-iitbhu','index/'+ file_name)
        object.put(Body=file,
                    Metadata={'FullName':instance.username})
    
    instance.profile.save()