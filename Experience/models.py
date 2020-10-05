from django.db import models

# Import Relational Tables
from Global.models import Skills
from Education.models import Other

class Experience(models.Model):
    experience_Image = models.ImageField(upload_to='images/')
    experience_Employer = models.CharField(max_length=200)
    experience_Title = models.CharField(max_length=200)
    experience_Title_Abbr = models.CharField(max_length=100, null=True)
    experience_Duration = models.CharField(max_length=200)
    experience_DOH = models.DateField(null=True)
    experience_DOL = models.DateField(blank=True, null=True)
    experience_Summary = models.TextField(max_length=1000)
    experience_Achievements = models.TextField(max_length=3000)
    experience_Courses = models.ManyToManyField(Other, blank=True, null=True)
    experience_Skills = models.ManyToManyField(Skills)

    class Meta:
        verbose_name_plural = "Experience"
        ordering = ['id']

    def __str__(self):
        return self.experience_Title

    def ach_as_list(self):
        return self.experience_Achievements.split(';')

    def doh_y(self):
        return self.experience_DOH.strftime('%Y')

    def job_sum(self):
        return self.experience_Summary[:200]

    def title_abbr(self):
        return self.experience_Title_Abbr
