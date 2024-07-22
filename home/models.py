from django.db import models

# Create your models here.

class Contact(models.Model):
    sno= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    phone= models.CharField(max_length=13)
    email= models.EmailField(max_length=100, null=True)
    subject= models.CharField(max_length=255)
    message= models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     
    def __str__(self):
        return self.name


class Reservation(models.Model):
    sno= models.AutoField(primary_key=True)
    reg_name= models.CharField(max_length=255,default=False)
    reg_phone= models.CharField(max_length=13)
    reg_email= models.EmailField(max_length=100, null=True)
    reg_date= models.CharField(max_length=10)
    reg_time= models.CharField(max_length=20)
    reg_person=models.CharField(max_length=10)
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     
    def __str__(self):
        return self.reg_name