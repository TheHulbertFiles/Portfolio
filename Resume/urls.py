from django.urls import path, include

from . import views

urlpatterns = [
    path('resume/', views.resume, name='resume'),
    path('', include('Education.urls')),
    path('', include('Experience.urls')),
    path('', include('Skills.urls')),
]