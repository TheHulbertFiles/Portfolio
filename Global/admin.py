from django.contrib import admin

# Register your models here.
from .models import Tags, Files, Social

mods = (Tags, Files, Social)

# Register
admin.site.register(mods)