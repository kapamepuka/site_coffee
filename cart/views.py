from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from cart.cart import Cart
from menu.models import Product
from django.http import HttpResponse

class CartView(View):
    def get(self, request):
        return HttpResponse()
    def post(self, request, id):
        cart = Cart(request)
        product = Product.objects.get(pk=id)
        cart.add(product)
        return HttpResponse()

    def delete(self, request, id):
        cart = Cart(request)
        product = Product.objects.get(pk=id)
        cart.remove(product)
        return HttpResponse()