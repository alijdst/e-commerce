from django.contrib import admin
from .models import Products, Category, Order, OrderItem, Cart, Payment, Comment, IsBuy


admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(Comment)
admin.site.register(IsBuy)