# Generated by Django 5.0.1 on 2024-01-23 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to='profile_images/'),
        ),
    ]