from django.shortcuts import render,redirect
from django.views import View


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from accounts.models import *
from feeds.models import Feed
from home.models import *


# Create your views here.
@method_decorator(login_required,name='dispatch')
class AdminHomeView(View):
    def get(self,request):
        if not request.user.is_superuser:
            return redirect("/")
        
        return render(request,'Admin_home.html')
    

@method_decorator(login_required,name='dispatch')
class AdminUserView(View):
    def get(self,request):
        users = Account.objects.all()
        return render(request,'Admin_users.html',{'users':users})

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