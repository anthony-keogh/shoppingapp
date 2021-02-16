from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from accounts.views import login
from products.forms import size_form
from django.contrib.auth.models import User
from products.models import Product_item
from django.urls import reverse

# Create your views here.

def coats(request):
    products = Product_item.objects.filter(name="brown coat")
    return render(request, 'coats.html', {'products':products})

def dresses(request):
    #products = Product_item.objects.filter(clothes_category=dresses)
    products = products = Product_item.objects.filter(name="red dress")
    return render(request, 'dresses.html', {'products':products})

def tops(request):
    products = products = Product_item.objects.filter(name="Black velvet top")
    return render(request, 'tops.html' , {'products':products})

def jeans(request):
    products = products = Product_item.objects.filter(name="Designer blue Jeans")
    return render(request, 'jeans.html', {'products':products})

def new_stock(request):
    products = Product_item.objects.all()
    return render(request, 'new_stock.html', {'products':products})



@login_required(login_url='login')
def loved_product(request):
  if request.method == 'GET':
    user = User.objects.get(username=request.user.username)
    
    return render(request, 'loved_product.html', { 'user': user})


def shop(request):
    

    return render(request, 'shop.html')

@login_required(login_url='login')
def product(request, pk):
    product = Product_item.objects.get(pk=pk)
    #products = Product_item.objects.all()
    if request.method=='POST':
        sizefittingform = size_form(request.POST)

        if sizefittingform.is_valid():

            sizefittingform.save()

            return redirect('purchase_product.html')
            
            
 
    else:
        sizefittingform = size_form()
        
    return render(request, "product.html",{'product':product,'sizefittingform':sizefittingform})



