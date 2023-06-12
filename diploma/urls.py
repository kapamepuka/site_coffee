from django.contrib import admin
from django.urls import path, include
from menu.views import MenuView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("menu/", MenuView.as_view()),
    path("cart/", include("cart.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
