from django.shortcuts import render  ,redirect
def counter(request):
    
    if 'Counte'  not in request.session:
        request.session['Counte'] = 1
    else:
        request.session['Counte']+=1      

    return render (request ,'counter.html')

def destroy_session(request):
    del request.session['Counte']
    return redirect('/')


# Create your views here.
