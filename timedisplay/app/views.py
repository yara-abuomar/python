from django.shortcuts import render 
from time import gmtime, strftime


def index(requst):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(requst,'index.html',context)

# Create your views here.
