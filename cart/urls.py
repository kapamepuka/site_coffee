from django.urls import path
from .views import add_to_cart, delete_item, decrement_item

urlpatterns = [
    path("add/<str:product_id>/", add_to_cart, name="cart-add"),
    path("delete/<str:product_id>/", delete_item, name="cart-delete"),
    path("decrement/<str:product_id>/", decrement_item, name="cart-decrement"),
]
