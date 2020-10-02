from django.contrib import admin
from .models import Artifact

# Combine Models
mods = (Artifact)

# Register Models
admin.site.register(mods)
