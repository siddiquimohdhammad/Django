from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import *
# from home.models import Product
# Create your views here.
def index (request):
    know={
        'info':'this is inforamtion from views to template'
    }
    # return HttpResponse('this is home page')
    return render(request,'index.html')
    

def abouts (request):
    # return HttpResponse('this is about page')
    
    return render(request,'about.html')

def services (request):
    if request.method=="POST":
        a=request.POST.get('a')
        b=request.POST.get('b')
        services=Product(a=a,b=b, date=datetime.today())
        services.save()
 
    return render(request,'services.html')

def contacts (request):
    # return HttpResponse('this is contact page')
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        num=request.POST.get('num')
        desc=request.POST.get('desc')
        contacts=Contact(name=name, email=email, num=num, desc=desc, date=datetime.today())
        contacts.save()

    return render(request,'contact.html')