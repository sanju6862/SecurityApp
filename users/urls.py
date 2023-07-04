from django.urls import path
from .views import home, profile, RegisterView,search_result

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('search_result/', search_result, name='search_result'),
]
