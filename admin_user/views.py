from django.shortcuts import render,redirect
from django.views import View


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from accounts.models import *
from feeds.models import Feed
from home.models import *
from store.models import *

# Create your views here.
@method_decorator(login_required,name='dispatch')
class AdminHomeView(View):
    def get(self,request):        
        return render(request,'Admin_home.html')
    

@method_decorator(login_required,name='dispatch')
class AdminUserView(View):
    def get(self,request):
        users = Account.objects.all()
        return render(request,'Admin_users.html',{'users':users})

@method_decorator(login_required,name='dispatch')
class AdminItemsView(View):
    def get(self,request,id=None):
        if id:
            Product.objects.get(id=id).delete()
            return redirect("/admin-user/items")

        items = Product.objects.all().order_by('-id')
        return render(request,'Admin_items.html',{'items':items})
    

@method_decorator(login_required,name='dispatch')
class AdminAddItemView(View):
    def get(self,request):
        return render(request,'Admin_add_item.html')
    
    def post(self,request):
        title = request.POST.get("title")
        price = request.POST.get("price")
        product_image = request.FILES.get("product_image")
        type_ = request.POST.get("type")

        Product.objects.create(title=title,price=price,product_type=type_,product_img=product_image)
        return redirect("/admin-user/items")
    

@method_decorator(login_required,name='dispatch')
class AdminOrdersView(View):
    def get(self,request,id=None):
        if id:
            order = Order.objects.get(id=id)
            order_items = OrderItems.objects.filter(order=order)
            return render(request,'Admin_view_order.html',{'order':order,"items":order_items})
        
        orders = Order.objects.all().order_by('-id')
        return render(request,'Admin_orders.html',{'orders':orders})

@method_decorator(login_required,name='dispatch')
class AdminNotiView(View):
    def get(self,request):
        notis = Notification.objects.all().order_by('-created_at')
        return render(request,'Admin_noti.html',{'notis':notis})
    
    def post(self,request):
        title = request.POST.get("title")
        content = request.POST.get("content")
        to_user = request.POST.get("to_user")

        Notification.objects.create(noti_to=to_user,noti_title=title,noti_desc=content)

        return redirect("/admin-user/notifications")
    

@method_decorator(login_required,name='dispatch')
class AdminFeedView(View):
    def get(self,request,id=None):
        if id:
            Feed.objects.filter(id=id).delete()
            return redirect("/admin-user/feeds")
        feeds = Feed.objects.all().order_by('-id')
        return render(request,'Admin_feeds.html',{'feeds':feeds})