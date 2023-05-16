from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('group-meetup/', views.group_meetup, name='group_meetup'),
    path('meeting-time-location-suggestion/', views.meeting_time_location_suggestion, name='meeting_time_location_suggestion'),
    path('notification/', views.notification, name='notification'),
    path('one-to-one-meetup/', views.one_to_one_meetup, name='one_to_one_meetup'),
    path('polling/', views.polling, name='polling'),
    path('register/', views.register, name='register'),
    # Add a custom handler for the 404 error
    path('404-error/', views.error_404, name='error_404'),
]
