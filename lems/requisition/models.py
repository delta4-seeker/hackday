from django.db import models
from user.models import UserProfile

class Requisition(models.Model):
    user= models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True, default= "0" , blank=True)
    total_compo = models.IntegerField()

class Requisition_compo(models.Model):
    requisition= models.ForeignKey(Requisition,on_delete=models.CASCADE,null=True, default= "0" , blank=True)
    user= models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True, default= "0" , blank=True)
    component= models.CharField(max_length=20)
    quantity = models.IntegerField()

 