from django.shortcuts import render ,redirect
from .models import *

def method(request):
    context={
        'alldojo':Dojo.read_dojo(),
        'allnin' :Ninja.read_ninja(),
    }
    return render(request ,'index.html',context)
    
def method2(request):
    Dojo.add_dojo(dojosname=request.POST['dojoname'] , dojoscity=request.POST['dojocity'] , dojosstate=request.POST['dojostate'])
    return redirect ('/')

def method4(request):
    Ninja.add_ninja(ninjafname=request.POST['fname'] ,ninjalname=request.POST['lname'], add=request.POST['dojoadd'])
    return redirect ('/')
def method3(request,id ):
    
    Dojo.dele_dojo( id)
    return redirect ('/')






# Create your views here.
