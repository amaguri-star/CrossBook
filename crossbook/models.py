from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.png', upload_to='profile_pics')
    text = models.TextField(blank=True, max_length=1000)

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="タイトル")
    content = models.TextField(max_length=5000, verbose_name="内容")
    image = models.ImageField(upload_to='post_pics', verbose_name="画像")
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")

    def __str__(self):
        return self.title
