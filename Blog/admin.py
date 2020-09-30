from django.contrib import admin

# Register your models here.
from .models import Post, Tags

mods = (Post, Tags)

# Register Social Links
admin.site.register(mods)