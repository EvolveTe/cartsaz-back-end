from django.contrib import admin
from store.models import CategoryModel, ProductModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'image']

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'code', 'category', 'description', 'showcase', 'image']
