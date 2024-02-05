from django.contrib import admin
from .models import Doubt


class DoubtAdmin(admin.ModelAdmin):
    list_display = ['user','topic','created_at']


# Register your models here.
admin.site.register(Doubt,DoubtAdmin)
