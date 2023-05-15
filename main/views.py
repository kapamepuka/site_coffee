from django.shortcuts import render
from django.http import  HttpResponse

from .models import Product


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def menu(request):
    return render(request, 'main/menu.html')



def test(request):
    product = Product.objects.all()
    return render(request, 'main/test.html', {"product": product})
