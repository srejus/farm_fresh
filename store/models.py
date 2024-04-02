from django.db import models
from accounts.models import Account


class Product(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    price = models.FloatField(default=0.0)
    product_img = models.ImageField(upload_to='product_image')
    product_type = models.CharField(max_length=50,null=True,blank=True)


class Cart(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='cart_user')
    item_name = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(default=0.0)


class Order(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='order_user')
    full_name = models.CharField(max_length=100,null=True,blank=True)
    number = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    pay_mode = models.CharField(max_length=10,default='COD')
    pincode = models.CharField(max_length=6,null=True,blank=True)
    total_price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='item_order')
    item_name = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(default=0.0)