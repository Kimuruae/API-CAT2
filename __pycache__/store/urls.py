from django.urls import path

from .views import getProduct, createProduct


urlpatterns = [
    path('product/', getProduct , name='getProduct'),
    path('product/create/', createProduct , name='createProduct'),
]