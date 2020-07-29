from django.shortcuts import render
from django.shortcuts import redirect, HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
#from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.urls import reverse

# Create your views here.

def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == 'POST':
        userform = UserRegistrationForm(request.POST)
        if userform.is_valid():
            userform.save()

             user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))
                                     
            messages.success(request, 'You have successfully created an account')
            return redirect('register')
 
    else:
        userform = UserRegistrationForm()
        context = {
        "userform": userform,
    }
 
    return render(request, "register.html",context)


def login(request):
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(
                username=request.POST["email_or_username"],
                password=request.POST["password"])
        
            if user:
                auth.login(request, user)
                messages.success(request, "You have logged in")
            
                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('profile'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()
           
    context = {
        "user_form": user_form,
    }
 
    return render(request, "login.html", context)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have now logged out')
    return redirect(reverse('index'))