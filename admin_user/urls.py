from django.urls import path
from .views import *

urlpatterns = [
    path('',AdminHomeView.as_view()),
    path('users',AdminUserView.as_view()),

    path('items',AdminItemsView.as_view()),
    path('items/delete/<int:id>',AdminItemsView.as_view()),
    path('items/add',AdminAddItemView.as_view()),

    path('orders',AdminOrdersView.as_view()),
    path('orders/<int:id>',AdminOrdersView.as_view()),

    path('feeds',AdminFeedView.as_view()),
    path('feeds/<int:id>',AdminFeedView.as_view()),
    path('notifications',AdminNotiView.as_view()),
]