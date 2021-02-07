from django.contrib import admin
from django.urls import include, re_path
from django.urls import path
from products.views import  product, shop
from django.conf.urls import url, include


urlpatterns = [
    path('', shop, name='shop'),
    #path('<int:id>/', product, name="product"),
    #path(r'^(?P<pk>\d+)/$', product, name="product")
    path(r'^product/(?P<pk>/d+)/$', product, name='product'),
    #url(r'^$', shop, name='shop'),
    #url(r'^(?P<pk>\d+)/$', product, name='product'),
]