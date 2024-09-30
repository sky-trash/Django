from django.db import models

class pr8_product(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to="book/%Y/%m/%d")
