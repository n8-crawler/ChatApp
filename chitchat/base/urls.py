from django.urls import path
from base import views

urlpatterns = [
    path('login/',views.loginform,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('registeruser/',views.registeruser,name='register'),
    path('profile/str<pk>',views.userprofile,name='profile'),
    path('updateprofile/str<pk>',views.updateuser,name='updateprofile'),

    path('',views.home,name='home'),
    path('room/str<pk>',views.room,name='room'),
    path('create-room/',views.create_room,name= 'create-room'),
    path('update-room/str<pk>',views.update_room,name= 'update-room'),
    path('delete-room/str<pk>',views.delete_room,name= 'delete-room')


]