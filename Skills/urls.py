from django.urls import path

from . import views

urlpatterns = [
    path('skills/', views.skills, name='skills'),
    path('skills/<int:Skill_id>/', views.skill_details, name='skill_details'),
]