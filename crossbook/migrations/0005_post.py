# Generated by Django 3.0.3 on 2021-02-05 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crossbook', '0004_profile_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=5000)),
                ('image', models.ImageField(upload_to='post_pics')),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
