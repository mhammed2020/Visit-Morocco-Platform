from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='about-01.jpg', upload_to='pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    
