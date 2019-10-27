from django.db import models

# Create your models here.


class neighbourhood(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    occupants = models.IntegerField()
     