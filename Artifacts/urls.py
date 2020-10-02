from django.urls import path

from . import views

urlpatterns = [
    path('artifacts/', views.artifacts, name='artifacts'),
    path('artifacts/<int:Artifact_id>/', views.artifact_detail, name='exhibit'),
]