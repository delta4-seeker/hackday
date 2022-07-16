from unicodedata import category
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    no_of_compo = models.IntegerField()



class Component(models.Model):
    category= models.ForeignKey(Category,on_delete=models.CASCADE,null=True, default= "0" , blank=True)

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=100)
    status = models.BooleanField(default=True)
    availability_qty = models.IntegerField()
    damage = models.BooleanField(default=False)
    available_data = models.TextField(max_length=50)
    

 

