from django.urls import path

from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('projects/<int:Project_id>/', views.project_detail, name='demos'),
]