from django.shortcuts import render ,redirect
import random 
def gold(request):
    request.session['golden']=0
    request.session['msg']=[]
    
    return render(request,'index.html')
def farm(request):
    if request.POST['which_form'] == 'Farm':
        num1= random.randint(2,5)
        request.session['golden']+=num1
        request.session['msg'].append("you entered a  farm and earned "+ str(num1))
        
    elif request.POST['which_form'] == 'Cave':
        num2=random.randint(5,10)
        request.session['golden']+=num2
        request.session['msg'].append("you entered a  cave and earned "+ str(num2))
        
    elif request.POST['which_form'] == 'house':
        num3=random.randint(10, 20)
        request.session['golden']+=num3
        request.session['msg'].append("you entered a  house and earned "+ str(num3))
    elif request.POST['which_form'] == 'Quest':
        num4=random.randint(-50, 50)  
        request.session['golden']+=num4
        if num4>0:
             request.session['msg'].append("you entered a  quest and earned "+ str(num4))
        else:
             request.session['msg'].append("you losted a  quest and earned "+ str(num4))

    return redirect('/final')
def final(request):
    return render(request,'index.html')

    

# Create your views here.
