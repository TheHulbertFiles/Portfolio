from django.contrib import admin

# Register your models here.
from .models import Tags, Files, Social, Skills

mods = (Tags, Files, Social, Skills)

# Register
admin.site.register(mods)