from django.db import models


class Artifacts(models.Model):
    artifacts_Title = models.CharField(max_length=200)
    artifacts_Image = models.ImageField(upload_to='images/')
    artifacts_Date = models.CharField(max_length=4)
    artifacts_Description = models.CharField(max_length=200)
    artifacts_Skills = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Artifacts"

    def __str__(self):
        return self.artifacts_Title