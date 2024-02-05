from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *

# Create your views here.

class LoginView(View):
    def get(self,request):
        err = request.GET.get("err")
        return render(request,'login.html',{'err':err})

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        err = "Invalid credentails!"
        return redirect(f"/account/login/?err={err}")
    

class SignupView(View):
    def get(self,request):
        err = request.GET.get("err")
        return render(request,'signup.html',{'err':err})
    
    def post(self,request):
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        pincode = request.POST.get("pincode")
        designation = request.POST.get("designation")
        exp = request.POST.get("exp")
        if exp == '':
            exp = 0

        if password1 != password2:
            err = "Password not matching!"
            return redirect(f"/accounts/signup?err={err}")
    
        user = User.objects.filter(username=username)
        if user.exists():
            err = "User with this username already exists"
            return redirect(f"/accounts/signup?err={err}")
        
        acc = Account.objects.filter(Q(email=email) | Q(phone=phone)).exists()
        if acc:
            err = "User with this phone or email already exists"
            return redirect(f"/accounts/signup?err={err}")
        
        user = User.objects.create_user(username=username,email=email,password=password1)
        acc = Account.objects.create(user=user,full_name=full_name,phone=phone,
                                     email=email,designation=designation,years_of_experience=exp,pincode=pincode)

        return redirect('/accounts/login')
        
        
        
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self,request):
        try:
            account = Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            return redirect("/")
        
        return render(request,'profile.html',{'profile':account})


class EditProfileView(View):
    def get(self,request):
        try:
            account = Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            return redirect("/")
        
        return render(request,'edit_profile.html',{'profile':account})
    
    def post(self,request):
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        pincode = request.POST.get("pincode")

        try:
            account = Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            return redirect("/")
        
        account.full_name = full_name
        account.email = email
        account.phone = phone
        account.pincode = pincode
        account.save()

        return redirect("/accounts/profile")