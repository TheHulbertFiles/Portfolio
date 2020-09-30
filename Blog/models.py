from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField

class Tags(models.Model):
    tag_Name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Tags"
        ordering = ['tag_Name']

    def __str__(self):
        return self.tag_Name

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_pub_date = models.DateTimeField()
    post_author = models.CharField(max_length=200)
    post_image = models.ImageField(upload_to='images/')
    post_body = RichTextField()
    post_mod_date = models.DateTimeField()
    post_tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.post_title

    def summary(self):
        return self.post_body[:200]

    def pub_date_mod(self):
        return self.post_pub_date.strftime('%B %e, %Y')

    def mod_date_f(self):
        return self.post_mod_date.strftime('%m/%d/%Y %H:%M:%S')