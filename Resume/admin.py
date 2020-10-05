from django.contrib import admin
from .models import Education, Experience, Courses, Other

mods = (Education, Experience, Courses, Other)

admin.site.register(mods)
