from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    menu=product.objects.all()[0:6]
    context={
        'menu':menu,

    }
    print(context,'yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
    # return HttpResponse("hello")
    return render(request,'index.html',context)