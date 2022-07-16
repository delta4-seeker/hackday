from msilib.schema import Component
from django.contrib import admin
from .models import Component


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'status',
                    'damage', 'available_data', 'availability_qty', 'category']
