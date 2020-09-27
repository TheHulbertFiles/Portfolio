from django.contrib import admin

from .models import Social, Section

mods = (Social, Section)

# Register Social Links
admin.site.register(mods)