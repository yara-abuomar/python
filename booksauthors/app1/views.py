from django.shortcuts import render ,redirect
from .models import *

def method(request):
    context={
        'allbook':Book.readbook()
    }
    return render(request,'addbook.html' ,context)

def method1(request):
    Book.addbook(tit=request.POST['title'],des=request.POST['description'])
    return redirect('/')

def method2(request):
    context={
        'allauthor':Author.readau()
    }
    return render(request,'addauthor.html' ,context)

def method3(request):
    Author.creatauth(first=request.POST['fname'],last=request.POST['lname'] ,note=request.POST['note'])
    return redirect('/author')
def method4(request ,id):
    context={
        'onebook':Book.bookinfo(num=id),
        'oneauthors':Author.readau()
    }
    return render(request ,'bookinfo.html',context)

def method5(request ,id1):
    context={
        'oneauthor':Author. authorinfo(num1=id1),
        'allbooks':Book.readbook()    
    }
    return render(request ,'authotrinfo.html',context)
def method6(request ,num):
    book1=Book.connectionbook(num)
    aut1=Author.objects.get(id=request.POST['author1'])
    aut1.books.add(book1)
    return redirect('/')

def method7(request ,num1):
    aothr1=Author.connectioauthor(num1)
    boo1=Book.objects.get(id=request.POST['book1'])
    aothr1.books.add(boo1)
    return redirect('/author')
    

 

# Create your views here.
