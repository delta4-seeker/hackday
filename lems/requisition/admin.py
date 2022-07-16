from django.contrib import admin
from .models import Requisition
from .models import Requisition_compo


@admin.register(Requisition)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['user','total_compo']

@admin.register(Requisition_compo)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ['user','component','quantity','requisition']

