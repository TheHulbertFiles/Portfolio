from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog/<int:Post_id>/', views.post_detail, name='post'),
]