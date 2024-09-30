from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    established = models.DateField()