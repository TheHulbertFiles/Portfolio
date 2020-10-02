from django.contrib import admin
from .models import Section

# Combine Models
mods = (Section)

# Register Models
admin.site.register(mods)