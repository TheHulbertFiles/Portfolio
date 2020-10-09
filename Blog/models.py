from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField

# Import Relational Tables
from Global.models import Skills, Tags

class Post(models.Model):
    post_Title = models.CharField(max_length=200)
    post_Pub_Date = models.DateTimeField()
    post_Author = models.CharField(max_length=200)
    post_Image = models.ImageField(upload_to='images/')
    post_Body = RichTextField()
    post_Mod_Date = models.DateTimeField()
    post_tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.post_Title

    def summary(self):
        return self.post_Body[:200]

    def pub_date_mod(self):
        return self.post_Pub_Date.strftime('%B %e, %Y')

    def mod_date_f(self):
        return self.post_Mod_Date.strftime('%m/%d/%Y %H:%M:%S')