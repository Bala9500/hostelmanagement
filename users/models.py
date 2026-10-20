from django.db import models

# Create your models here.
class TenetDetails(models.Model):
    name= models.CharField(max_length=255)
    age= models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    phone= models.CharField(max_length=255)
    aadhaar_number=models.CharField(max_length=255)
    room_no=models.CharField(max_length=255,default='not assigned')
    username = models.CharField(max_length=255, default='olduser')
    password = models.CharField(max_length=255, default='temp123')
    payment=models.CharField(max_length=255,default='Not Paid')


class ReportDetails(models.Model):
    tenant = models.ForeignKey(TenetDetails,on_delete=models.CASCADE,null=True,blank=True)
    about = models.CharField(max_length=255)
    description = models.CharField(max_length=600)
    status = models.CharField(max_length=50, default='Pending')


