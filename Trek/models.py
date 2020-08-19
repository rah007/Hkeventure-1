from django.db import models
from datetime import datetime,timedelta,date
from django.utils import timezone
from django.core.validators import MaxValueValidator
# Create your models here.

class Trek(models.Model):
    Name      = models.CharField(max_length=100, default='None')
    Last_Name = models.CharField(max_length=100,default='None')
    Adventure = models.CharField(max_length = 100,default='None')
    Trek_Date = models.DateField()
    Email     = models.CharField(max_length=120,default='None' )
    Mob_No    = models.IntegerField(validators=[MaxValueValidator(9999999999)],default=0000000000)
    Country   = models.CharField(max_length = 100,default='None' )
    State     = models.CharField(max_length = 100,default='None' )
    Zip       = models.IntegerField(validators=[MaxValueValidator(999999)],default=000000)
    paymentMethod = models.CharField(max_length = 100,default='None')
    Pay_ID    = models.CharField(max_length = 100,default='None')
    Total_count=models.IntegerField(validators=[MaxValueValidator(99)],default=000000)
    terms = models.CharField(max_length=100, default='None')
    Book_Date = models.DateField()
    # kk = models.IntegerField(default = 00)
    
    def __str__(self):
        return self.Name
    
class Details(models.Model):
    Name      = models.CharField(max_length=100, default='None')
    Last_Name = models.CharField(max_length=100,default='None')
    Adventure = models.CharField(max_length = 100,default='None')
   # description = models.CharField(max_length = 500, default='None')
    Email     = models.CharField(max_length=120,default='None' )
    Mob_No    = models.IntegerField(validators=[MaxValueValidator(9999999999)],default=0000000000)
    message   = models.CharField(max_length = 500,default='None' )
    # State     = models.CharField(max_length = 100,default='None' )

    
    def __str__(self):
        return self.Name

