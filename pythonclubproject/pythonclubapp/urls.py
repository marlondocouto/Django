from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name='index'), #empty quotes work only for index pages. 
    path('getResources/', views.getResources, name='resources'),
]

