from django.contrib import admin

# Register your models here.
from .models.category import Category
from .models.customer import Customer
from .models.product import Products
from .models.orders import Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone','email',)
    list_filter = ('first_name','last_name','phone','email',)
    search_fields = ('first_name','last_name','phone','email',)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','price','category','description',)
    list_filter = ('name','price','category',)
    search_fields = ('name','price','category',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product','customer','quantity','price','address','phone', 'date', 'status')
    list_filter = ('product','customer','quantity','price','address','phone', 'date', 'status')
    search_fields = ('product','customer','quantity','price','address','phone', 'date', 'status')