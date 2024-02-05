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
        feeds = Feed.objects.exclude(posted_by__user=request.user)
        return render(request,'feeds.html',{'feeds':feeds,'current_user':user})


class LikeUnlike(View):
    def get(self,request,id,uid):
        usr = Account.objects.get(id=uid)
        post = Feed.objects.get(id=id)
        post.total_likes += 1
        post.save()

        try:
            Likes.objects.get(liked_by=usr,post=post).delete()
            return JsonResponse({"status":"disliked"})

        except:
            Likes.objects.create(liked_by=usr,post=post)
            return JsonResponse({"status":"liked"})
