from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.png', upload_to='profile_pics')
    text = models.TextField(blank=True, max_length=1000)

    def __str__(self):
        return f'{self.user.username} Profile'
