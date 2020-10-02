from django.db import models

class Social(models.Model):
    social_Link = models.CharField(max_length=200)
    social_SiteName = models.CharField(max_length=200)
    social_FaClass = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Social Links"

    def __str__(self):
        return self.social_SiteName
        
class Tags(models.Model):
    tag_Name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Tags"
        ordering = ['tag_Name']
    
    def __str__(self):
        return self.tag_Name

class Files(models.Model):
    file_Name = models.CharField(max_length=200)
    file_Upload = models.FileField(upload_to='files/')
    file_Icon = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Files"
        ordering = ['file_Name']
    
    def __str__(self):
        return self.file_Name