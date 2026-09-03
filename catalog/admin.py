from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'size_in_inches', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('title', 'description')

from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)