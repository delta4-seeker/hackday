from django.db import models 
from user.models import UserProfile
 


class Quotation(models.Model):
    user= models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True, default= "0" , blank=True)
    component = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.BooleanField(default=True)
