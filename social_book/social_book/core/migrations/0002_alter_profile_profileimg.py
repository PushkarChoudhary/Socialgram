# Generated by Django 4.0.5 on 2022-07-11 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank_profile_picture.png', upload_to='profile_images'),
        ),
    ]
