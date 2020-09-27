from django.urls import path

from . import views

urlpatterns = [
    path('artifacts/', views.artifacts, name='artifacts'),
]