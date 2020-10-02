from django.contrib import admin
from .models import Post

# Combine Models
mods = (Post)

# Register Models
admin.site.register(mods)