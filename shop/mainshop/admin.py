from django.contrib import admin
from .models import Products, Category, Order, OrderItem, Cart


admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)