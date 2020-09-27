from django.db import models

class Social(models.Model):
    social_Link = models.CharField(max_length=200)
    social_SiteName = models.CharField(max_length=200)
    social_FaClass = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Social Links"

    def __str__(self):
        return self.social_SiteName

    
class Section(models.Model):
    section_Title = models.CharField(max_length=200)
    section_Image = models.ImageField(upload_to='images/')
    section_Description = models.CharField(max_length=200)
    section_Link = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Highlights"
        ordering = ['section_Title']

    def __str__(self):
        return self.section_Title