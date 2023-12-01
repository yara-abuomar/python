from django.shortcuts import render ,redirect
from.models import *
from django.contrib import messages
import bcrypt

def form(request):
    return render(request ,'index.html')

def registrationuser(request):
    errors=User.objects.basic_valedater(request.POST)
    if len(errors)>0:
        for key ,value in errors.items():
            messages.error(request ,value)
        return redirect('/')
    else:
        password=request.POST['pass']
        pass1=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        usr=User.objects.create(first_name=request.POST['fname'],Last_name=request.POST['lname'],email=request.POST['email'],password=pass1)
        request.session['user']=usr.id
        request.session['name']=request.POST['fname']
        return redirect ('/suc')
    
def log (request):
    user1=User.objects.filter(email=request.POST['email'])
    if user1:
        user=user1[0]
        if bcrypt.checkpw(request.POST['pass'].encode(),user.password.encode()):
            request.session['user']=user.id
            request.session['name']=user.first_name
            return redirect ('/suc')
        else:
            messages.error(request,"incorrect username or password")
            return redirect ("/")
    else:
            messages.error(request,"incorrect username or password")
            return redirect ("/")
    
def logout(request):
    request.session.flush()
    return redirect('/')


def succses(request):
    if 'user' not in request.session:
        messages.error(request ,"you must log in first !")
        return redirect('/')
    context={
       
        'oneuser':User.objects.get(id=int(request.session['user'])),
        'allmsg':Msg.objects.all().order_by("-id"),
    }
    return render(request,'wall.html',context)
 
def addmsg(request):
    onemsg=Msg.objects.create(massege=request.POST['msg'],user=User.objects.get(id=request.session['user']))
    return redirect('/suc')

def addcomment(request,num):
    Comment.objects.create(Comment=request.POST['com'],user=User.objects.get(id=request.session['user']),msg=Msg.objects.get(id=int(num)))
   
    return redirect('/suc')

def delete (request,num1):
    msgg=Msg.objects.get(id=int(num1))
    if Msg.user.id == request.session['user']:
        msgg.delete()
    else:
        messages.error(request,"can delete by user only")
    return redirect('/suc')



# Create your views here.
