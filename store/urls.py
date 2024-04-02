from django.urls import path
from .views import *

urlpatterns = [
    path('',StoreView.as_view()),
    path('add-to-cart/<int:id>',AddCartView.as_view()),
    path('remove-to-cart/<int:id>',RemoveCartView.as_view()),
    path('cart',CartView.as_view()),
    path('success',SuccessView.as_view()),
    path('my-orders',MyOrdersView.as_view()),
    path('my-orders/<int:id>',MyOrdersView.as_view()),
    path('place-order',PlaceOrderView.as_view())
]