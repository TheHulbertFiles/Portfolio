from django.contrib import admin
from .models import Experience

# Combine Models
mods = (Experience)

# Register Models
admin.site.register(mods)