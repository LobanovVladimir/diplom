from unicodedata import name
from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

class places(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(decimal_places=3,max_digits=20)
    longtitude = models.DecimalField(decimal_places=3,max_digits=20)
    usersname =models.ForeignKey(users,models.CASCADE)
    description = models.CharField(max_length=2000)
    def __str__(self) -> str:
        return self.name

