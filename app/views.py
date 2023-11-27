from django.shortcuts import render ,redirect
from.models import *
def addform(request):
    
    context={
        'item':Product.objects.all()
    }
    return render(request ,'form.html',context)

def add(request,id):
    if 'buy' not in request.session:
          request.session['buy']=int(request.POST['quantity'])
    else:
          request.session['buy'] +=int(request.POST['quantity'])
          
    p1=Product.objects.get(id=int(id))
    pri=p1.price
    
    if 'pric' not in request.session:
         request.session['pric']=pri *int(request.POST['quantity'])
    else:
         request.session['pric']+=pri*int(request.POST['quantity'])
         
    return redirect ('/show/' +str(id))

def des(request):
     del request.session['buy']
     del request.session['pric']
     return redirect('/')

def one(request,num):
     context={
        'add':Product.objects.get(id=int(num)),
        
    }
     return render (request ,'check.html',context)

     

# Create your views here.
