from django.db import models 
from user.models import UserProfile
 


class Quotation(models.Model):
    user= models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True, default= "0" , blank=True)
    component = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)