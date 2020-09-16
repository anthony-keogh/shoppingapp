"""shoopingapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import login
from home.views import index
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.urls import path 
from django.conf.urls.static import static
from accounts.views import register, login, profile
 #, detail_update_view
#from addresses.views import list, form, prev_address, update
#from billing.views import payment_method
from carts.views import your_cart #, loved_product #cart_clicked 
#from orders.views import library, order_detail, order_list
from products.views import dresses, coats, tops, jeans, new_stock, product, loved_product #likeProduct #, loved_product
from billing.views import purchase_product
from products import urls as products_urls
from django.urls import include, re_path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index' ),
    #path('400/',TemplateView.as_view(template_name="400.html"), name='400'),
    #path('403/',TemplateView.as_view(template_name="403.html"), name='403'),
    #path('404/',TemplateView.as_view(template_name="404.html"), name='404'),
    #path('500/',TemplateView.as_view(template_name="500.html"), name='500'),
    #path('detail_update_view/',detail_update_view, name='detail_update_view'),
    #path('404/', permission_denied_view),
    path('about/',TemplateView.as_view(template_name="about.html"), name='about'),
    path('design/',TemplateView.as_view(template_name="design.html"), name='design'),
    path('styles/',TemplateView.as_view(template_name="styles.html"), name='styles'),
    path('material/',TemplateView.as_view(template_name="material.html"), name='material'),
    path('whatstrending/',TemplateView.as_view(template_name="whatstrending.html"), name='whatstrending'),
    path('register/',register, name='register'),
    path('profile/',profile, name='profile'),
    path('login/',login, name='login'),
    path('product/', include(products_urls)),
    path('coats/',coats, name='coats'),
    path('jeans/',jeans, name='jeans'),
    path('new_stock/',new_stock, name='new_stock'),
    path('tops/',tops, name='tops'),
    path('dresses/',dresses, name='dresses'),
    path('product/',product, name='product'),
    path('your_cart/',your_cart, name='your_cart'),
    path('loved_product/',loved_product, name='loved_product'),
    path('product', product, name="product"),
    #path('accounts/login/?next=/loved_product/',error_login, name='error_login'),
    #path('prev_address/',prev_address, name='prev_address'),
    #path('list/',list, name='list'),
    #path('form/',form, name='form'),
    #path('sales/',sales, name='sales'),
    path('purchase_product/',purchase_product, name='purchase_product'),
    #path('like_category/',like_category, name='like_category'),
    #path('checkout_done/',checkout_done, name='checkout_done'),
    #path('checkout/',checkout, name='checkout'),
    #path('home/',home, name='home'),
    #path('library/',library, name='library'),
    #path('order_list/',order_list, name='order_list'),
    #path('order_detail/',order_detail, name='order_detail'),
    #path('detail/',detail, name='detail'),
    #path('feature_detail/',feature_detail, name='feature_detail'),
    #path('list/',list, name='list'),
    #path('user_history/',user_history, name='user_history'),
]

