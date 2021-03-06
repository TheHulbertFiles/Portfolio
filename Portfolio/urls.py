from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('', include('Artifacts.urls')),
    path('', include('Blog.urls')),
    path('', include('Projects.urls')),
    path('', include('Resume.urls')),
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)