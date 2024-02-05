from django.db import models
from accounts.models import Account

# Create your models here.
class Doubt(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='doubt_asked_by')
    topic = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField(null=True,blank=True)
    answered_by = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='doubt_answered_by',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # can know when anwered