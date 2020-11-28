from django.contrib import admin
from .models import Product,Category

# class AdminProduct(admin.ModelAdmin):
#     list_display = ['name', 'price', 'Category']

# class AdminCategory(admin.ModelAdmin):
#     list_display = ['name']

admin.site.register(Product)
admin.site.register(Category)
