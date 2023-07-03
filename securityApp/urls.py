from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from LostFound.views import item_recovery, item_search, lost_and_found, report_found_item
from PanicButton.views import location_sender, panic_button
from facialsearch.views import facialsearch
from incidentreporting.views import report_incident, view_incident
from map.views import map_view
from notifications.views import notification_view
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView, show_profile
from complaints.views import *
from Emergency_contacts.views import Emergency_contacts

from users.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('users.urls')),

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('create_complaint/',create_complaint,name = 'create_complaint'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('view_complaints/',view_complaints,name = 'view_complaints'),
    path('update_complaint_status/',update_complaint_status,name = 'update_complaint_status'),
    path('emergency_contacts',Emergency_contacts,name = 'emergency_contacts'),
    path('facialsearch/',facialsearch,name = 'facialsearch'),
    path('notifications/',notification_view,name = 'notifications'),
    path('report_incident/', report_incident, name='report_incident'),
    path('incidents/', view_incident, name='view_incident'),
    path('profile/<int:profile_id>/', show_profile, name='show_profile'),
    path('lost-and-found/', lost_and_found, name='lost_and_found'),
    path('report-found-item/', report_found_item, name='report_found_item'),
    path('lost_item_search/', item_search, name='lost_item_search'),
    path('recover/<int:item_id>/', item_recovery, name='item_recovery'),
    path('map/', map_view, name='map'),
    path('panic_button/',panic_button,name = 'panic_button'),
    path('location_sender/',location_sender,name = 'location_sender'),
    
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),

] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)