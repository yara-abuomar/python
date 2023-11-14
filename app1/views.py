from django.shortcuts import render ,redirect
import random	

def guees(request):
    request.session['num']=random.randint(1, 100)
    print(request.session['num'])
    

    return render(request,'form.html')

def handle(request):
       
        request.session['number']=int(request.POST['guess'])
        num1=request.session['number'] 

        if num1 < request.session['num']:
            
            return redirect('/low')
        elif num1==request.session['num']:
            return redirect('/correct')
        
        else:
            
            return redirect('/high')
    
def low(request):
    return render(request,'form.html')
def high(request):
    return render(request,'form.html')
def correct(request):
    return render(request,'correct.html')







    

# Create your views here.
