from django.urls import path
from . import  views
from cart.views import CartView

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('api/cart', CartView.as_view(), name='cart'),





]