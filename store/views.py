from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Sum

from .models import *


@method_decorator(login_required, name='dispatch')
class StoreView(View):
    def get(self,request):
        items = Product.objects.all()
        return render(request,'store.html',{'items':items})


@method_decorator(login_required, name='dispatch')
class AddCartView(View):
    def get(self,request,id):
        qnty = "1"
        # item_id = request.GET.get("item_id")
        acc = Account.objects.get(user=request.user)

        item = Product.objects.get(id=id)
        total = int(qnty)*item.price

        cart = Cart.objects.filter(user=acc,item_name=item.title)

        if cart.exists():
            cart = cart.last()
            cart.quantity += 1
            total = cart.quantity*item.price
            cart.total_price = total
            cart.save()
        else:
            Cart.objects.create(user=acc,item_name=item.title,quantity=1,total_price=total)
        return redirect("/store/")
    


@method_decorator(login_required, name='dispatch')
class RemoveCartView(View):
    def get(self,request,id):
        qnty = "1"
        # item_id = request.GET.get("item_id")
        acc = Account.objects.get(user=request.user)

        item = Product.objects.get(id=id)
        total = int(qnty)*item.price

        cart = Cart.objects.filter(user=acc,item_name=item.title)

        if cart.exists():
            cart = cart.last()
            if cart.quantity == 1:
                cart.delete()
            else:
                cart.quantity -= 1
                total = cart.quantity*item.price
                cart.total_price = total
                cart.save()
       
        return redirect("/store/")
    

@method_decorator(login_required, name='dispatch')
class CartView(View):
    def get(self,request):
        cart = Cart.objects.filter(user__user=request.user)
        total_price_sum = cart.aggregate(total_price_sum=Sum('total_price'))['total_price_sum']
        if total_price_sum is None:
            total_price_sum = 0

        return render(request,'cart.html',{'products':cart,'total_price_sum':total_price_sum})
    

@method_decorator(login_required, name='dispatch')
class MyOrdersView(View):
    def get(self,request,id=None):
        orders = Order.objects.filter(user__user=request.user).order_by('-id')
        if id:
            order_items  =  OrderItems.objects.filter(order__id=id)
            return render(request,'my_order_view.html',{'orders':order_items})
        return render(request,'my_orders.html',{'orders':orders})
    

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
        total_price = 0.0
        for item in cart:
            total_price += item.total_price
            OrderItems.objects.create(order=order,item_name=item.item_name,total_price=item.total_price,quantity=item.quantity)
        
        order.total_price = total_price
        order.save()
        cart.delete()

        # online payment
        if pay_mode == 'PAY_ONLINE':
            from farmer_media.utils import create_stripe_payment_link
            pay_url = create_stripe_payment_link(total_price)
            return redirect(pay_url)
        
        return render(request,'success.html',{'is_cod':True})
    

class SuccessView(View):
    def get(self,request):
        return render(request,'success.html')