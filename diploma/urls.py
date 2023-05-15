from django.contrib import admin
from django.urls import path, include
from menu.views import MenuView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('menu/', MenuView.as_view()),
]
