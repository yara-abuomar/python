from django.db import models
import re
from datetime import date

class UserManager(models.Manager):
    def basic_validater(self,postData):
        errors={}
        if len(postData['fname'])<2:
            errors['fname']="firstname should be 2 char atleast"
        fname_regex=re.compile(r'^[a-zA-Z]')
        if not fname_regex.match(postData['fname']):
            errors['fname']="firstname should be char only "
        if len(postData['lname'])<2:
            errors['lname']="lastname should be 2 char atleast"
        #if postData['birth']< date.MINYEAR("2010"):
           # errors['birth']="the age should be more 13"
        lname_regex=re.compile(r'^[a-zA-Z]')
        if not lname_regex.match(postData['lname']):
            errors['lname']="lastname should be char only "
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = "Invalid email address!"
        if len(User.objects.filter(email=postData['email']))>0:
            errors['email']="Email should be unieq!"
        if len(postData['pass'])<8:
            errors['pass']="password should be 8 char atleast"
        if postData['pass'] != postData['confirm']:
            errors['confirm']="password dont match"
        return errors
        

        

class BookManager(models.Manager):
    def validation(seld,postData):
        error={}
        if len(postData['title1'])<1:
            error['title1']="title should be added"
        if len(postData['desc'])<8:
            error['desc']="description  should be 8 char atleast"
        return error
     
class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    #birthday=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class Book(models.Model):
    title=models.CharField(max_length=45)
    Descriptionn=models.TextField()
    user_upload=models.ForeignKey(User,related_name="uploaded_books",on_delete=models.CASCADE)
    users_fav=models.ManyToManyField(User,related_name="like_books")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=BookManager()



# Create your models here.
