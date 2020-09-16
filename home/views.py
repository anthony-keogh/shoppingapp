from django.shortcuts import render
from products.models import Product_item

# Create your views here.
def index(request):
    products = Product_item.objects.all()
    return render(request, 'index.html',{'products':products})