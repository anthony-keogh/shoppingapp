from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from .forms import cart_form
#from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
#from .forms import Snippet
#from .serializers import SnippetSerializer
# Create your views here.


@login_required(login_url='login')
def your_cart(request):
    return render(request, 'your_cart.html')

#@csrf_exempt
#def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    #if request.method == 'GET':
     #   snippets = Snippet.objects.all()
      #  serializer = SnippetSerializer(snippets, many=True)
      #  return JsonResponse(serializer.data, safe=False)

    #elif request.method == 'POST':
      #  data = JSONParser().parse(request)
      #  serializer = SnippetSerializer(data=data)
       # if serializer.is_valid():
        #    serializer.save()
        #    return JsonResponse(serializer.data, status=201)
       # return JsonResponse(serializer.errors, status=400)
    
#@login_required(login_url='login')
#def like_cart(request):

   # clicking_cart = None
    #if request.method == 'POST':
     #   clicking_cart = cart_form(request.POST)

    #like_1 = 0
    #if clicking_cart:
      #  cart = Cart.objects.get(id=int(clicking_cart))
        #if cart:
           # like_1 = cart.like_1 + 1
           # cart.like_1 =  like_1
           # cart.save()
            
    

    #return HttpResponse(like_1)
           
            


