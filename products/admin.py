from django.contrib import admin

# Register your models here.
from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Products, ProductsAdmin)