from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view()),
    path('ask-doubt',AskDoubtView.as_view()),
    path('doubts/profile/<int:id>',MyDoubts.as_view()),
    path('doubts/delete/<int:id>/<int:pro_id>',DeleteDoubt.as_view()),
]