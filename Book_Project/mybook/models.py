from django.db import models

# Create your models here.

class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.FloatField()
    