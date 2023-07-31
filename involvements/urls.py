from django.urls import path
from involvements import views

urlpatterns = [
    path('add/<int:user_id>/',views.add_involvement, name='add_involvement'),
    path('view/<int:user_id>/', views.view_involvements, name = 'view_involvements'),
    path('update/<int:involvement_id>/', views.update, name = 'update_involvement'),
    path('delete/<int:involvement_id>/', views.delete, name = 'delete_involvement'),
]
