from django.urls import path,include
from base.api import views
from rest_framework.authtoken import views as t_views
from rest_framework_simplejwt import views as jwt_views
urlpatterns=[
    path('room/',views.getrooms),
    path('room/<str:pk>',views.getroom),
    path('jwt/',jwt_views.TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('jwt_refresh/',jwt_views.TokenRefreshView.as_view(),name='token_refresh'),
    
  
             



]
