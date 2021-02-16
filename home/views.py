from django.shortcuts import render
from products.models import Product_item

# Create your views here.
def index(request):
    productscoat = Product_item.objects.filter(name="brown coat")
    productsdress = Product_item.objects.filter(name="red dress")
    productstops = Product_item.objects.filter(name="Black velvet top")
    return render(request, 'index.html',  {'productscoat':productscoat, 'productsdress': productsdress, 'productstops':productstops})