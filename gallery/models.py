from pickle import TRUE
from django.db import models

# Create your models here.
    
    
# class Category(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100, null=False, blank=False)
#     images = models.ImageField(null=True, blank=False, upload_to='gallery/Category')

    
#     def __str__(self):
#         return self.name
     
class Gallery(models.Model):
    # category = models.ForeignKey(Category,on_delete=models.CASCADE )
    image = models.ImageField(null=False, blank=False,upload_to='gallery/image')
    alt = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self):
        return self.alt
