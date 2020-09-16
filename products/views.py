from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from accounts.views import login
from products.forms import size_form
from django.contrib.auth.models import User
from products.models import Product_item

# Create your views here.

def coats(request):
    
    return render(request, 'coats.html')

def dresses(request):
    return render(request, 'dresses.html')

def tops(request):
    return render(request, 'tops.html')

def jeans(request):
    return render(request, 'jeans.html')

def new_stock(request):
    return render(request, 'new_stock.html')

#def product(request):
#    return render(request, 'product.html')

@login_required(login_url='login')
def loved_product(request):
  if request.method == 'GET':
    user = User.objects.get(username=request.user.username)
    
    return render(request, 'loved_product.html', { 'user': user})


def product_page(request):
    products = Product_item.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop.html', context)

@login_required(login_url='login')
def product(request):
    products = Product_item.objects.all()
    if request.method=='POST':
        sizefittingform = size_form(request.POST)

        if sizefittingform.is_valid():

            sizefittingform.save()

            return redirect('purchase_product.html')
            
            
 
    else:
        sizefittingform = size_form()
        
    return render(request, "product.html",{'sizefittingform':sizefittingform,'products':products})



