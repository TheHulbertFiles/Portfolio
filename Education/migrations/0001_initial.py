# Generated by Django 3.1.1 on 2020-10-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Global', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_Year', models.DateField()),
                ('course_Term', models.CharField(max_length=100)),
                ('course_Degree', models.CharField(max_length=100)),
                ('course_Dept', models.CharField(max_length=100)),
                ('course_Abbr', models.CharField(max_length=100)),
                ('course_Number', models.CharField(max_length=100)),
                ('course_Name', models.CharField(max_length=200)),
                ('course_Grade', models.CharField(blank=True, max_length=200)),
                ('course_Description', models.TextField(blank=True, max_length=3000)),
            ],
            options={
                'verbose_name_plural': 'Courses',
                'ordering': ['course_Year'],
            },
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_Year', models.DateField()),
                ('other_Name', models.CharField(max_length=200)),
                ('other_Organization', models.CharField(max_length=200)),
                ('other_Progress', models.CharField(blank=True, max_length=200)),
                ('other_Description', models.TextField(blank=True, max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Other Courses',
                'ordering': ['-other_Year'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_Image', models.ImageField(upload_to='images/')),
                ('education_University', models.CharField(max_length=500)),
                ('education_Degree', models.CharField(max_length=500)),
                ('education_Dates', models.CharField(max_length=200)),
                ('education_Graduation_Year', models.DateField(blank=True, null=True)),
                ('education_GPA', models.CharField(max_length=200)),
                ('education_Description', models.TextField(max_length=2000)),
                ('education_Courses', models.ManyToManyField(to='Education.Courses')),
                ('education_Skills', models.ManyToManyField(to='Global.Skills')),
            ],
            options={
                'verbose_name_plural': 'Education',
                'ordering': ['-education_Graduation_Year'],
            },
        ),
    ]
