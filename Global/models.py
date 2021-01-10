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

    # Variables
    fileType_Choices = (
        ("--", "--"),
        ("docx","docx"),
        ("pdf","pdf"),
        ("xlsx","xlsx"),
        ("pptx","pptx"),
        ("image","image")
    )

    file_Name = models.CharField(max_length=200)
    file_Upload = models.FileField(upload_to='files/')
    file_Icon = models.CharField(max_length=200)
    file_Description = models.CharField(max_length=200)
    file_Type = models.CharField( 
        max_length = 20, 
        choices = fileType_Choices, 
        default = '--'
        )
    
    class Meta:
        verbose_name_plural = "Files"
        ordering = ['file_Name']
    
    def __str__(self):
        return self.file_Name

class Skills(models.Model):
    
    # Variables
    skill_Levels = (
        ('Beginner','Beginner'),
        ('Junior','Junior'),
        ('Advanced','Advanced')
    )
    
    skill_Types = (
        ('Technical','Technical'),
        ('Soft','Soft'),
        ('Other','Other')
    )

    skill_Categories = (
        ('Admin','Admin'),
        ('Back-End','Back-End'),
        ('Databases','Databases'),
        ('DevOps','DevOps'),
        ('Front-End','Front-End'),
        ('General','General'),
        ('Leadership','Leadership'),
        ('Projects','Projects'),
        ('Software','Software'),
        ('Systems','Systems'),
        ('Web App Dev','Web App Dev')
    )

    skill_Type = models.CharField(max_length=100, choices=skill_Types)
    skill_Category = models.CharField(max_length=100, choices=skill_Categories)
    skill_Name = models.CharField(max_length=100)
    skill_Icon = models.CharField(max_length=100)
    skill_Description = models.TextField(max_length=500)
    skill_Years = models.DecimalField(max_digits=5, decimal_places=2)
    skill_Level = models.CharField(max_length=200, choices=skill_Levels)

    class Meta:
        verbose_name_plural = "Skills"
        ordering = ['-skill_Years']

    def __str__(self):
        return self.skill_Name

    def tech_skills():
        t_skills = Skills.objects.all().filter(skill_Type='Technical')
        return t_skills

    def other_skills():
        o_skills = Skills.objects.all().filter(skill_Type='Other')
        return o_skills

    def soft_skills():
        s_skills = Skills.objects.all().filter(skill_Type='Soft')
        return s_skills