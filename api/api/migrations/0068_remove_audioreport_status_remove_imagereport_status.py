# Generated by Django 4.2.11 on 2024-06-28 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0067_alter_audiodecisionthrough_media_obj_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audioreport',
            name='status',
        ),
        migrations.RemoveField(
            model_name='imagereport',
            name='status',
        ),
    ]
