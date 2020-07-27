from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from accounts.views import login
from products.forms import size_form

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
def your_cart(request):
    return render(request, 'your_cart.html')

@login_required(login_url='login')
def loved_product(request):
    return render(request, 'loved_product.html')


@login_required(login_url='login')
def product(request):
    if request.method=='POST':
        sizefittingform = size_form(request.POST)
        if sizefittingform.is_valid():
            sizefittingform.save()
            #messages.success(request, 'You have successfully created an account')
            
 
    else:
        sizefittingform = size_form()
        
    return render(request, "product.html",{'sizefittingform':sizefittingform})
