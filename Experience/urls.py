from django.urls import path

from . import views

urlpatterns = [
    path('experience/', views.experience, name='experience'),
    path('experience/<int:Exp_id>/', views.exp_details, name='exp_details'),
]