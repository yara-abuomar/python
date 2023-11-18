from django.db import models

class Dojo(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def add_dojo( dojosstate ,dojosname , dojoscity  ):
          Dojo.objects.create(name=dojosname ,city=dojoscity ,state=dojosstate)
    def read_dojo():
          return Dojo.objects.all()
    def dele_dojo(id):
          new=Dojo.objects.get(id=int(id))
          return new.delete()



class Ninja(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    dojo=models.ForeignKey(Dojo ,related_name="ninjas" ,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def add_ninja(ninjafname, ninjalname , add):
         Ninja.objects.create(first_name=ninjafname ,last_name=ninjalname , dojo=Dojo.objects.get(id=int(add)))
    def read_ninja():
         return Ninja.objects.all()

# Create your models here.
