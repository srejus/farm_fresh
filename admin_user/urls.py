from django.urls import path
from .views import *

urlpatterns = [
    path('',AdminHomeView.as_view()),
    path('users',AdminUserView.as_view()),
    path('feeds',AdminFeedView.as_view()),
    path('feeds/<int:id>',AdminFeedView.as_view()),
    path('notifications',AdminNotiView.as_view()),
]