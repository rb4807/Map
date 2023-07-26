from django.db import models

# Create your models here.

class Table(models.Model):
    city = models.TextField(max_length=100)
    location= models.TextField(max_length=100)
    name= models.TextField(max_length=100)
    coordinates= models.FloatField()