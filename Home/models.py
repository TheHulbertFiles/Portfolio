from django.db import models
    
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