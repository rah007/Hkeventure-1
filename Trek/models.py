from django.db import models
from datetime import datetime,timedelta,date
from django.utils import timezone
# Create your models here.

class Trek(models.Model):
    Name      = models.CharField(max_length=100, default='Individual')
    Last_Name = models.CharField(max_length=100,default='Individual')
    Adventure = models.CharField(max_length = 100,default='Individual')
    # Trek_Date = models.DateField(default=timezone.now)
    Email     = models.CharField(max_length=120,default='Individual' )
    Mob_No    = models.IntegerField(default=0000000000)
    Country   = models.CharField(max_length = 100,default='Individual' )
    State     = models.CharField(max_length = 100,default='Individual' )
    Zip       = models.IntegerField(default=000000)
    paymentMethod = models.CharField(max_length = 100,default='Individual')
    Pay_ID    = models.CharField(max_length = 100,default='Individual')
    # Book_Date = models.DateField(default=timezone.now)
    # pincode       = models.IntegerField()
    

    
    # def __str__(self):
    #     return self.Name

