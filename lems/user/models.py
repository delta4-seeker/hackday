from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    roll = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
