# Generated by Django 3.0.3 on 2021-02-01 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crossbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile.jpg', upload_to='profile_pics'),
        ),
    ]
