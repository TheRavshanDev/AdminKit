# Generated by Django 3.2.9 on 2022-04-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220421_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users-avatar'),
        ),
    ]
