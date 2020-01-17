from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hood(models.Model):
   admin = models.ForeignKey(User,on_delete=models.CASCADE, default = 1)
   name = models.CharField(max_length =30)
   location = models.CharField(max_length =30)
   occupants_count = models.IntegerField
   
class User(models.Model):
   name = models.CharField(max_length =30)
   hood = models.ForeignKey(Hood, on_delete=models.CASCADE,default = 1) 

class Business(models.Model):
   name = models.CharField(max_length =30)
   hood = models.ForeignKey(Hood,on_delete=models.CASCADE, default = 1)
   biz_email =  models.CharField(max_length =30)