from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=45)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def addbook(tit,des):
         Book.objects.create(title=tit,description=des)
    def readbook():
        return Book.objects.all()
    def bookinfo(num):
        return Book.objects.get(id=int(num))
    def connectionbook(num):
        return Book.objects.get(id=int(num))


class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    notes=models.TextField()
    books=models.ManyToManyField(Book,related_name="authors")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def creatauth(first,last,note):
        Author.objects.create(first_name=first,last_name=last,notes=note)
    
    def readau():
        return Author.objects.all()
    
    def authorinfo(num1):
        return Author.objects.get(id=int(num1))
    def connectioauthor(num1):
        return Author.objects.get(id=int(num1))
    
    



# Create your models here.
