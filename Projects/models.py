from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField

# Import Relational Tables
from Global.models import Tags, Files, Skills

class Project(models.Model):
    project_Title = models.CharField(max_length=200)
    project_Image = models.ImageField(upload_to='images/')
    project_Year = models.CharField(max_length=4)
    project_Institute = models.CharField(max_length=200)
    project_Type = models.CharField(max_length=200)
    project_Description = RichTextField()
    project_Skills = models.ManyToManyField(Skills)
    project_Link = models.URLField(max_length = 200)

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.project_Title

    def summary(self):
        return self.project_Description[:200]