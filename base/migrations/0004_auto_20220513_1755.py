# Generated by Django 3.2.9 on 2022-05-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_enrolledtutorial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialmedia',
            name='video_description',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutorialmedia',
            name='video_name',
            field=models.CharField(default='default', max_length=300),
            preserve_default=False,
        ),
    ]
