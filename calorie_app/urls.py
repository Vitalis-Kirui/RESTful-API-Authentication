from django.urls import path, include
from calorie_app import views

urlpatterns = [
    path('', include('djoser.urls')), 
    path('', include('djoser.urls.authtoken')), 
]