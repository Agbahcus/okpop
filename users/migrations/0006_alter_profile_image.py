# Generated by Django 4.0.6 on 2022-08-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='FB_IMG_16040545884204163.jpg', upload_to='profile_pics'),
        ),
    ]
