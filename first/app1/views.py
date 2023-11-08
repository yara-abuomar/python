from django.shortcuts import render , HttpResponse ,redirect
from django.http import JsonResponse
def root (requst):
    return redirect('/blogs')

def index(requst):
    return HttpResponse("placeholder to later display a list of all blogs")
def new (requst):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create (requst):
    return redirect("/" )
def show (requst,number):
    return HttpResponse("placeholder to display blog number:" + str(number))
def edit (requst,number):
    return HttpResponse("placeholder to edit blog "+ str(number))
def destroy (requst,number):
    return redirect("/blogs")
def redirected_method (requst):
    return JsonResponse ({"title":"my first blog","contetnt":"lorem,ipsum dolor"})

# Create your views here.
 