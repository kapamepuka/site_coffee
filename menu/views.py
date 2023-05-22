
# Create your views here.
from django.views.generic import TemplateView
from .models import Product

class MenuView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, *args, **kwargs):
        products = Product.objects.all()
        print(products)
        context = super(MenuView, self).get_context_data(*args, **kwargs)
        context['products'] = products
        return context