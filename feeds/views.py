from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *

# Create your views here.
@method_decorator(login_required, name='dispatch')
class FeedView(View):
    def get(self,request):
        user = Account.objects.get(user=request.user)
        feeds = Feed.objects.exclude(posted_by__user=request.user).order_by('-id')
        return render(request,'feeds.html',{'feeds':feeds,'current_user':user})


class LikeUnlike(View):
    def get(self,request,id,uid):
        usr = Account.objects.get(id=uid)
        post = Feed.objects.get(id=id)
        

        try:
            Likes.objects.get(liked_by=usr,post=post).delete()
            post.total_likes -= 1
            post.save()
            return JsonResponse({"status":"disliked"})

        except:
            Likes.objects.create(liked_by=usr,post=post)
            post.total_likes += 1
            post.save()
            return JsonResponse({"status":"liked"})


@method_decorator(login_required, name='dispatch')
class CreatePostView(View):
    def get(self,request):
        return render(request,'create_post.html')
    
    def post(self,request):
        content = request.POST.get("content")
        tags = request.POST.get("tags")

        try:
            acc = Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            print("\n-------No Account Instance found----------\n")
            return redirect("/feeds/")
        
        Feed.objects.create(posted_by=acc,post_content=content,tags=tags)
        return redirect("/feeds/")