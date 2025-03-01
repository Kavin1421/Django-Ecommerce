from django.contrib import admin
from .models import * #it will import all the classes from models.py
from .models import Order

# class Categoryadmin(admin.ModelAdmin):
#     list_display = ('fname','image','desc')
# admin.site.register(Catagory,Categoryadmin)

class Categoryadmin(admin.ModelAdmin):#it will inherits an Admin module from admin
    list_display = ('fname',) #list_display is an keyword to display in front of the admin page
admin.site.register(Catagory,Categoryadmin)#it will send the Category class with the Catagoryadmin to the admin page
admin.site.register(Products,Categoryadmin)#it will returns asusuall like before

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'product__fname', 'id')
    ordering = ('-created_at',)
    list_editable = ('status',)  # Allows editing directly in the admin list view

admin.site.register(Order, OrderAdmin)
