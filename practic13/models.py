from django.db import models
from django.contrib.auth.models import User


class Gender(models.TextChoices):
    MEN="Мужской"
    WOMEN="Женский"

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    gender= models.CharField(choices=Gender, blank=True, max_length=20)
    country= models.CharField(max_length=100, blank=True)
    city= models.CharField(max_length=100, blank=True)
    street= models.CharField(max_length=100, blank=True)
    house= models.CharField(max_length=100, blank=True)
    apartament_number= models.CharField(max_length=100, blank=True)
