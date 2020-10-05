from django.contrib import admin
from .models import Education, Other, Courses

# Combine Models
mods = (Education, Other, Courses)

# Register Models
admin.site.register(mods)