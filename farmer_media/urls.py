from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('agri-officer',include('agri_officer.urls')),
    path('accounts/',include('accounts.urls')),
    path('admin-user/',include('admin_user.urls')),
    path('feeds/',include('feeds.urls')),
    path('store/',include('store.urls')),
]
