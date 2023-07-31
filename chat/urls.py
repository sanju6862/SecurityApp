# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('chat/<int:id1>/<int:id2>/', views.chat, name='chat'),
    # More URL patterns...
]