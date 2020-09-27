# Generated by Django 3.1.1 on 2020-09-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artifacts_Title', models.CharField(max_length=200)),
                ('artifacts_Image', models.ImageField(upload_to='images/')),
                ('artifacts_Date', models.CharField(max_length=4)),
                ('artifacts_Description', models.CharField(max_length=200)),
                ('artifacts_Skills', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Artifacts',
            },
        ),
    ]
