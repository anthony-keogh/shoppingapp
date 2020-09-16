from django.contrib import admin
from django.urls import include, re_path
from django.urls import path
from products.views import product_page, product


urlpatterns = [
    #path('', product_page, name='shop'),
    path('product', product, name="product"),
]