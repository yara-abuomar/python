from django.db import models
import re
class UserManager(models.Manager):
    def basic_valedater(self,postData):
        errors={}
        if len(postData['fname'])<2:
            errors['fname'] ="First name should be at least two character"
        fname_regex=re.compile(r'^[a-zA-Z]')
        if  not fname_regex.match(postData['fname']):
            errors['fname'] ="First name should be character only !"
        if len(postData['lname'])<2:
            errors['lname'] ="Last name should be at least two character"
        lname_regex=re.compile(r'^[a-zA-Z]')
        if  not lname_regex.match(postData['lname']):
            errors['lname'] ="Last name should be character only !"
        if len(postData['email'])<0:
            errors['email'] ="emmail  must be added !"
        email_regex=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(postData['email']):
            errors['email'] ="Invalid email!"
        if len(User.objects.filter(email=postData['email'])) >0:
            errors['email'] ="Email should be uniqe"
        if len(postData['pass']) <8:
            errors['pass'] = "Password should be at least 8 character"
        if postData['pass'] != postData['confirm']:
            errors['confirm'] ="password dont match" 
        return errors  
        
class User (models.Model):
    first_name=models.CharField(max_length=255)
    Last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

   

class Msg (models.Model):
    massege=models.TextField()
    user=models.ForeignKey(User,related_name="msgs" ,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def showmsg():
        return Msg.objects.all()
    

class Comment (models.Model):
    Comment=models.TextField()
    user=models.ForeignKey(User,related_name="comments" ,on_delete=models.CASCADE)
    msg=models.ForeignKey(Msg,related_name="comments" ,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
# Create your models here.
