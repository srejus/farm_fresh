from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    AGRICULTURAL_OFFICER = 'AGRICULTURAL_OFFICER'
    USER_TYPE_CHOICES = (
        ('FARMER','FARMER'),
        ('AGRICULTURAL_OFFICER','AGRICULTURAL_OFFICER'),
        ('ADMIN','ADMIN'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    pincode = models.CharField(max_length=6,null=True,blank=True)
    designation = models.CharField(max_length=100,null=True,blank=True)
    years_of_experience = models.IntegerField(default=0)
    gender = models.CharField(max_length=6,null=True,blank=True)
    user_type = models.CharField(max_length=30,choices=USER_TYPE_CHOICES,default='FARMER')

    def __str__(self):
        return str(self.full_name)
