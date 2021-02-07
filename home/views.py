from django.shortcuts import render
from products.models import Product_item

# Create your views here.
def index(request):
    
    return render(request, 'index.html')