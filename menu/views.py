from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class MenuView(TemplateView):
    template_name = 'menu.html'

    #def get(self, request):