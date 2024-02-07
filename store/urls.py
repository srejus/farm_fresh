from django.urls import path
from .views import *

urlpatterns = [
    path('',StoreView.as_view()),
    path('add-to-cart',AddCartView.as_view()),
    path('cart',CartView.as_view()),
    path('place-order',PlaceOrderView.as_view())
]