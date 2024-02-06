from django.urls import path
from .views import *

urlpatterns = [
    path('',FeedView.as_view()),
    path('like-unlike/<int:id>/<int:uid>',LikeUnlike.as_view()),
    path('create-post',CreatePostView.as_view()),
]