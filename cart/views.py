# Create your views here.
from cart.cart import Cart
from django.http.response import JsonResponse, HttpResponse
from menu.models import Product

def add_to_cart(request, product_id: int):
    cart = Cart(request)
    product = Product.objects.get(pk=product_id)
    data = cart.add(product_id, product.name, price=product.price)
    if data is None:
        return JsonResponse({"exist": True})

    return JsonResponse(data)

def delete_item(request, product_id: int):
    cart = Cart(request)
    cart.delete(product_id)
    return HttpResponse()



def decrement_item(request, product_id: int):
    cart = Cart(request)
    cart.decrement(product_id)
    return HttpResponse()
