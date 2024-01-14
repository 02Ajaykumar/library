from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    
class Book(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    category = models.CharField(max_length=100)
    author = models.TextField(max_length=100,default='J.K Rowling')
    publication = models.TextField(max_length=100,default='/-')
    description = models.TextField(max_length=200,default='/-')
    availability = models.TextField(max_length=100,default='0')