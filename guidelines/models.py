# models.py
from django.db import models

class Guideline(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
     return self.title


class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
     return self.title

class Media(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='media/')

    def __str__(self):
     return self.title