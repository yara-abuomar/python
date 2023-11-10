from django.shortcuts import render ,redirect
def creatform(request):
    return render(request,"index.html")

def handle (request):
       request.session['name']=request.POST['fname']
       request.session['loc']=request.POST['Location']
       request.session['lan']=request.POST['languge']
       request.session['comm']=request.POST['comment']
   
       
       return redirect("/result") 
        
def result (request):
    return render(request,"result.html")


# Create your views here.
