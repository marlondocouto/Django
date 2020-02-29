from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'), #empty quotes work only for index pages. 
    path('getResources/', views.getResources, name='resources'),
    path('getMeetings/', views.getMeetings, name='meetings'),
    path('meetingDetails/<int:id>', views.meetingDetails, name='meetingdetails'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('newResource/', views.newResource, name='newresource'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
   
]

