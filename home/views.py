from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from accounts.models import Account
from .models import Doubt,Notification

# Create your views here.
class IndexView(View):
    def get(self,request):
        notis = Notification.objects.filter(noti_to='FARMER').order_by('-id')
        return render(request,'index.html',{'notis':notis})
    

@method_decorator(login_required, name='dispatch')
class AskDoubtView(View):
    def get(self,request):
        return render(request,'ask_doubt.html')
    
    def post(self,request):
        topic = request.POST.get("topic")
        question = request.POST.get("question")
        try:
            acc = Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            return redirect("/")
        
        # saving the doubt in the db
        Doubt.objects.create(user=acc,topic=topic,question=question)
        return redirect("/")
    

@method_decorator(login_required, name='dispatch')
class MyDoubts(View):
    def get(self,request,id):
        doubts = Doubt.objects.filter(user__id=id).order_by('-id')
        return render(request,'my_doubts.html',{'questions':doubts})


@method_decorator(login_required, name='dispatch')
class DeleteDoubt(View):
    def get(self,request,id,pro_id):
        try:
            doubt = Doubt.objects.get(id=id,user__user=request.user)
        except Exception:
            return redirect("/")
        
        doubt.delete()
        return redirect(f"/doubts/profile/{pro_id}")