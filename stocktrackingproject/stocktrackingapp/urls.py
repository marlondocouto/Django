from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettype/', views.gettype, name='type'),
    path('getperformances/', views.getperformances, name='performances'),
    path('getresources/', views.getresources, name='resources'),
    path('newStockType/', views.newStockType, name='newStockType'),
    path('newStockPerformance/', views.newStockPerformance, name='newStockPerformance'),
    path('newFinanceResource/', views.newFinanceResource, name='newFinanceResource'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]