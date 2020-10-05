from django.db import models

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
    experience_Courses = models.CharField(max_length=200, blank=True, null=True)
    experience_Skills = models.TextField(max_length=500)

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

class Education(models.Model):
    education_Image = models.ImageField(upload_to='images/')
    education_University = models.CharField(max_length=500)
    education_Degree = models.CharField(max_length=500)
    education_Dates = models.CharField(max_length=200)
    education_Graduation_Year = models.DateField(blank=True, null=True)
    education_GPA = models.CharField(max_length=200)
    education_Description = models.TextField(max_length=2000)
    education_Skills = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "Education"
        ordering = ['-education_Graduation_Year']

    def __str__(self):
        return self.education_Degree

    def grad_y(self):
        return self.education_Graduation_Year.strftime('%Y')

    def degree_abbr(self):
        if self.education_Degree[:4] == 'B.A.':
            return "Bachelor of Arts"
        else:
            return "Associate of Science"

    def specialization(self):
        return self.education_Degree[5:100]

    def degree_sum(self):
        return self.education_Description[:200]

class Other(models.Model):
    other_Year = models.DateField()
    other_Name = models.CharField(max_length=200)
    other_Organization = models.CharField(max_length=200)
    other_Progress = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Other Courses"
        ordering = ['-other_Year']

    def __str__(self):
        return self.other_Name

class Courses(models.Model):
    course_Year = models.DateField()
    course_Term = models.CharField(max_length=100)
    course_Degree = models.CharField(max_length=100)
    course_Dept = models.CharField(max_length=100)
    course_Abbr = models.CharField(max_length=100)
    course_Number = models.CharField(max_length=100)
    course_Name = models.CharField(max_length=200)
    course_Grade = models.CharField(max_length=200, blank=True)
    course_Description = models.TextField(max_length=3000)

    class Meta:
        verbose_name_plural = "Courses"
        ordering = ['course_Year']

    def __str__(self):
        course = self.course_Abbr + ' ' + self.course_Number + ' - ' + self.course_Name
        return courses
    
    def coursesFilter(Edu_degree):
        courses_f = Courses.objects.filter(course_Degree=Edu_degree)
        return courses_f