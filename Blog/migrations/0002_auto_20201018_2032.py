# Generated by Django 3.1.1 on 2020-10-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Global', '0001_initial'),
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_author',
            new_name='post_Author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_body',
            new_name='post_Body',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_image',
            new_name='post_Image',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_mod_date',
            new_name='post_Mod_Date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_pub_date',
            new_name='post_Pub_Date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_title',
            new_name='post_Title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_tags',
        ),
        migrations.AddField(
            model_name='post',
            name='post_Tags',
            field=models.ManyToManyField(to='Global.Tags'),
        ),
    ]
