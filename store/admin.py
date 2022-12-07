from django.contrib import admin
from .models import *


# Register your models here
class Product_Category_Admin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    ordering = ['id']


class Manufacturer_Admin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    ordering = ['id']


class Product_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cat', 'mnf']
    list_display_links = ['id', 'name']
    ordering = ['id']



admin.site.register(Product_Category, Product_Category_Admin)
admin.site.register(Manufacturer, Manufacturer_Admin)
admin.site.register(Product, Product_Admin)
