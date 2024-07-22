
from contextlib import nullcontext
from distutils.command.upload import upload
from unicodedata import category, name
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    images = models.ImageField(null=True, blank=True, upload_to='menu/icons')

    
    def __str__(self):
        return self.name
     
class Menu(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False,upload_to='menu/images')
    alt = models.CharField(max_length=250, null=True, blank=False)
    
    def __str__(self):
        return self.name
    