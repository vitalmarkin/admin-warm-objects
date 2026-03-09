from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import ProductListAPI, ProductDetailAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductListAPI.as_view()),
    path('api/products/<slug:slug>/', ProductDetailAPI.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)