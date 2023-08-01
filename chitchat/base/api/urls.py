from django.urls import path,include
from base.api import views

urlpatterns=[
    path('room/',views.getrooms),
    path('room/<str:pk>',views.getroom),
  
             



]
