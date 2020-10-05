from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField

# Import Relational Tables
from Global.models import Skills, Files, Tags

class Artifact(models.Model):
    artifact_Title = models.CharField(max_length=200)
    artifact_Image = models.ImageField(upload_to='images/')
    artifact_Year = models.CharField(max_length=4)
    artifact_Institute = models.CharField(max_length=200)
    artifact_Type = models.CharField(max_length=200)
    artifact_Description = RichTextField()
    artifact_Skills = models.ManyToManyField(Skills)
    artifact_Files = models.ManyToManyField(Files)

    class Meta:
        verbose_name_plural = "Artifacts"

    def __str__(self):
        return self.artifact_Title

    def summary(self):
        return self.artifact_Description[:200]