from django.urls import path

from . import views

urlpatterns = [
    path('education/', views.education, name='education'),
    path('education/<int:Edu_id>/<str:Edu_degree>/', views.edu_details, name='edu_details'),
    path('courses/<int:Course_id>/', views.course_details, name='course_details'),
]