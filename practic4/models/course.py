from django.db import models

class Course(models.Model): 
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    students = models.ManyToManyField('Student')