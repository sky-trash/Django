from django.db import models

class Book(models.Model): 
    title= models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publishers = models.ManyToManyField('Publisher')
    image = models.ImageField(upload_to="book/%Y/%m/%d",null=True)
