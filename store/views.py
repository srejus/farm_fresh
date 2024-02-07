from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *


@method_decorator(login_required, name='dispatch')
class StoreView(View):
    def get(self,request):
        items = Product.objects.all()
        return render(request,'store.html',{'items':items})


@method_decorator(login_required, name='dispatch')
class AddCartView(View):
    def get(self,request):
        qnty = request.GET.get("qnty")
        item_id = request.GET.get("item_id")
        acc = Account.objects.get(user=request.user)

        item = Product.objects.get(id=item_id)
        total = int(qnty)*item.price
        if int(qnty) == 0:
            Cart.objects.filter(user=acc,item_name=item.title).delete()
        else:
            Cart.objects.create(user=acc,item_name=item.title,quantity=qnty,total_price=total)
        return redirect("/store/")
    

@method_decorator(login_required, name='dispatch')
class CartView(View):
    def get(self,request):
        cart = Cart.objects.filter(user__user=request.user)
        return render(request,'cart.html',{'products':cart})
    

@method_decorator(login_required, name='dispatch')
class PlaceOrderView(View):
    def post(self,request):
        full_name = request.POST.get("full_name")
        number = request.POST.get("number")
        email = request.POST.get("email")
        address = request.POST.get("address")
        pincode = request.POST.get("pincode")
        pay_mode = request.POST.get("pay_mode")

        acc = Account.objects.get(user=request.user)

        order = Order.objects.create(
            user=acc,full_name=full_name,number=number,email=email,address=address,pincode=pincode,pay_mode=pay_mode
        )
        cart = Cart.objects.filter(user=acc)
        for item in cart:
            OrderItems.objects.create(order=order,item_name=item.item_name,total_price=item.total_price,quantity=item.quantity)
        
        cart.delete()
        return redirect("/")