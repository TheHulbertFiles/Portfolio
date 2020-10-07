# Generated by Django 3.1.1 on 2020-10-07 16:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Global', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artifact_Title', models.CharField(max_length=200)),
                ('artifact_Image', models.ImageField(upload_to='images/')),
                ('artifact_Year', models.CharField(max_length=4)),
                ('artifact_Institute', models.CharField(max_length=200)),
                ('artifact_Type', models.CharField(max_length=200)),
                ('artifact_Description', ckeditor.fields.RichTextField()),
                ('artifact_Files', models.ManyToManyField(to='Global.Files')),
                ('artifact_Skills', models.ManyToManyField(to='Global.Skills')),
            ],
            options={
                'verbose_name_plural': 'Artifacts',
            },
        ),
    ]
