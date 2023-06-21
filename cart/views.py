# Create your views here.
from cart.cart import Cart
from django.http.response import JsonResponse, HttpResponse
from menu.models import Product

def add_to_cart(request, product_id: int):
    print(product_id)
    cart = Cart(request)
    product = Product.objects.get(pk=product_id)
    print(product)
    data = cart.add(product_id, product.name, price=product.price)
    return JsonResponse(data)

def delete_item(request, product_id: int):
    print(product_id)
    print("delete:", product_id)
    cart = Cart(request)
    cart.delete(product_id)
    return HttpResponse()
