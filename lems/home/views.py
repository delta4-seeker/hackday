from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
from components.models import Category
from requisition.models import Requisition

def category(request):
    categories = Category.objects.all()
    context = {
        "category" : categories , 
    }

    queryset = Category.objects.all().values()
    return JsonResponse({"category": list(queryset)})

def unseen_request(request):
    unseen_request = Requisition.objects.filter(status = 'unseen')
    context = {
        "unseen_request" : unseen_request , 
    }

    queryset = Category.objects.all().values()
    return JsonResponse({"category": list(queryset)})


