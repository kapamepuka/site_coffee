from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from cart.cart import Cart

class MenuView(TemplateView):
    template_name = 'menu.html'

    def get(self, request):