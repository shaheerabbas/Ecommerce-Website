from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Category

def index(request):
    products = Product.get_all_produts()
    categories = Category.get_all_categories()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request,"index.html", data)