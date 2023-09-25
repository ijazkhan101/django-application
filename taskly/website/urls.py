from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home),
    path('index/', home),
    path('about/',  about),
    path('services/', services),
    path('emp/', include('emp.urls')),
    path("student/", student_home)


]
