from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

def index(request):
    prds = Product.get_all_produts()

    return render(request,"index.html", {'products': prds})