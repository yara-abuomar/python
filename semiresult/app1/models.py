from django.db import models
from datetime import date
class Show (models.Model):
    title=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    releasedate =  models.DateField(("Date"), default=date.today)
    description=models.TextField()
    creates_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def creatshow(network1,title1,description1,reldate):
        return Show.objects.create(title=title1,network=network1,description=description1,releasedate =reldate)
    def readshow():
        return Show.objects.all()
    def readone():
       return Show.objects.last()
# Create your models here.
