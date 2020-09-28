from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('<int:Post_id>/', views.detail, name='detail'),
]