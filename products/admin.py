from django.contrib import admin

#django
from django.contrib import admin

#models
from products.models import Products


@admin.register(Products)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'stock']
    list_display_links = ['name']
    list_editable = ['description', 'price']
    search_fields = ['created_at']
    list_filter = ['created_at']
