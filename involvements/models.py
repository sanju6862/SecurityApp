from django.db import models
from django.contrib.auth.models import User

class Involvement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    action_taken = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} - {self.user}"
