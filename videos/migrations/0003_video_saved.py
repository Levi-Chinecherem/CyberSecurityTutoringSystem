# Generated by Django 4.2.4 on 2023-08-23 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_alter_video_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='saved',
            field=models.BooleanField(default=False),
        ),
    ]
