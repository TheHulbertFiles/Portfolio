from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField

# Import Relational Tables
from Global.models import Tags, Files

class Artifact(models.Model):
    artifacts_Title = models.CharField(max_length=200)
    artifacts_Image = models.ImageField(upload_to='images/')
    artifacts_Date = models.CharField(max_length=4)
    artifacts_Description = RichTextField()
    artifacts_Skills = models.ManyToManyField(Tags)
    artifacts_Files = models.ManyToManyField(Files)

    class Meta:
        verbose_name_plural = "Artifacts"

    def __str__(self):
        return self.artifacts_Title

    def summary(self):
        return self.artifacts_Description[:200]