from django.contrib import admin

from .models import Project

# Combine Models
mods = (Project)

# Register Models
admin.site.register(mods)
