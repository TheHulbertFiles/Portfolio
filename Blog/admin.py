from django.contrib import admin

# Register your models here.
from .models import Post

mods = (Post)

# Register Social Links
admin.site.register(mods)