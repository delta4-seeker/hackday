from msilib.schema import Component
from django.contrib import admin
from .models import Component
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','no_of_compo']

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'status',
                    'damage', 'available_data', 'availability_qty']
