from email.mime import image
from statistics import mode
from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.CharField(max_length=100,unique=True)
    description = models.TextField(max_length=255,blank=True)
    image = models.ImageField( upload_to="images/categories",blank =True )
    def __str__(self):
        return self.name


    