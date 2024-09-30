from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=10, null=True, blank=True)
    year = models.CharField(max_length=10, null=True, blank=True)
    
class Author(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)