from django.db import models
from django.contrib.auth.models import User
import PIL
from PIL import Image

# Create your models here.


class Neighbourhood(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    occupants = models.IntegerField()
     
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(default = 'default.jpg', upload_to ='profile_pics')
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = PIL.Image.open(self.pic.path)

        if img.height > 300 or img.width >300:
            output_size = (152,152)
            img.thumbnail(output_size)
            img.save(self.pic.path)


class Business(models.Model):
    name = models.CharField(max_length = 30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()
    