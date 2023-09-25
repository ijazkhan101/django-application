"""
URL configuration for taskly project.
"""
from django.contrib import admin
from django.urls import path, include
from website.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('Student/home', include('website.urls')),
]
