from django.shortcuts import render,redirect
from django.views import View


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from accounts.models import *
from feeds.models import Feed
from home.models import *


# Create your views here.
@method_decorator(login_required,name='dispatch')
class ArgiHomeView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        if acc.user_type != Account.AGRICULTURAL_OFFICER:
            return redirect("/")
        
        return render(request,'agri_home.html')


@method_decorator(login_required,name='dispatch')
class AgriDoubts(View):
    def get(self,request,id=None):
        acc = Account.objects.get(user=request.user)
        if acc.user_type != Account.AGRICULTURAL_OFFICER:
            return redirect("/")
        
        doubts = Doubt.objects.all()
        return render(request,'agri_doubts.html',{'doubts':doubts})

    def post(self,request,id=None):
        doubt = Doubt.objects.get(id=id)
        ans = request.POST.get("ans")
        acc = Account.objects.get(user=request.user)
        doubt.answer = ans
        doubt.answered_by = acc
        doubt.save()

        return redirect("/agri-officer/doubts")



@method_decorator(login_required,name='dispatch')
class AgriNotiView(View):
    def get(self,request):
        notis = Notification.objects.filter(noti_to=Notification.AGRICULTURAL_OFFICER).order_by('-created_at')
        return render(request,'agri_noti.html',{'notis':notis})