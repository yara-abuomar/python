from django.shortcuts import render ,redirect
from.models import *
from django.contrib import messages
import bcrypt
def registrationandlogin(request):
    return render(request ,'form.html')
def registration(request):
    errors=User.objects.basic_validater(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        password=request.POST['pass']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user1=User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'],password=pw_hash)
        request.session['id']=user1.id
        request.session['name']=user1.first_name
        return redirect('/books')
def login(request):
    user1=User.objects.filter(email=request.POST['email'])
    if user1:
        user=user1[0]
        if bcrypt.checkpw(request.POST['pass'].encode(), user.password.encode()):
            request.session['id']=user.id
            request.session['name']=user.first_name
            return redirect('/books')
        else:
            messages.error(request,"incorrect username or password")
            return redirect ("/")
    else:
            messages.error(request,"incorrect username or password")
            return redirect ("/")

def bookform(request):
    if 'id' not in request.session:
        messages.error(request,"you must log in ")
        return redirect ('/')
    context={
        'allbook':Book.objects.all()
    }
    return render (request,'bookform.html',context)

def addbook (request):
    error=Book.objects.validation(request.POST)
    if len(error)>0:
        for key,value in error.items():
            messages.error(request,value)
        return redirect('/books')
    else:
        book1=Book.objects.create(title=request.POST['title1'],Descriptionn=request.POST['desc'],user_upload=User.objects.get(id=request.session['id']))
        request.session['book']=book1.id
        request.session['bookname']=book1.title
        user1=User.objects.get(id=request.session['id'])
        book=Book.objects.last()
        book.users_fav.add(user1)
        return redirect('/books')
    
def logout(request):
    request.session.flush()
    return redirect('/')

def vieworupdate (request ,id):
    if 'id' not in request.session:
        messages.error(request,"you must log in ")
        return redirect ('/')
    user1=Book.objects.get(id=int(id)).user_upload
 
    if request.session['id']== user1.id:
        
        context={
            'onebook':Book.objects.get(id=int(id)),
            'which':1
        }
        return  render(request,'final.html',context)
    else:
        
        context={
            'onebook':Book.objects.get(id=int(id)),
            'which':2
        }
        return  render(request,'final.html',context)
    
def delete(request ,num ,num1):
    if request.session['id']!=User.objects.get(id=int(num1)):
        book1=Book.objects.get(id=int(num))
        book1.delete()
        return redirect ('/books')
    else:
        messages.error(request,"You are not the user who upload the book ")
        return redirect ('/books/'+str(num))
    
def updatbook(request,id1,id2):
    if request.session['id']!=User.objects.get(id=int(id2)):
        book1=Book.objects.get(id=int(id1))
        book1.title=request.POST['title1']
        book1.Descriptionn=request.POST['desc']
        book1.save()
        return redirect ('/books')
    else:
        messages.error(request,"You are not the user who upload the book ")
        return redirect ('/books/'+str(id1))
    

def addfav(request,idbook):
    user1=User.objects.get(id=request.session['id'])
    book1=Book.objects.get(id=int(idbook))
    book1.users_fav.add(user1)
    return redirect ('/books/'+str(idbook))

def unfav(request ,numbook):
    user1=User.objects.get(id=request.session['id'])
    book1=Book.objects.get(id=int(numbook))
    book1.users_fav.remove(user1)
    return redirect ('/books/'+str(numbook))




    
    



















   

# Create your views here.
