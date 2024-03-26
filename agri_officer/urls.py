from django.urls import path
from .views import *

urlpatterns = [
    path('',ArgiHomeView.as_view()),
    path('/doubts',AgriDoubts.as_view()),
    path('/doubts/<int:id>',AgriDoubts.as_view()),
    path('/notifications',AgriNotiView.as_view()),
]