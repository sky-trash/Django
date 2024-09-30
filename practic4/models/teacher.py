from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    birth_day = models.DateField()