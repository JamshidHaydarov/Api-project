from django.contrib import admin
from .models import *


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'busket',
        'product',
        'quantity'
    )
    list_filter = (
        ('quantity', admin.BooleanFieldListFilter),
    )


@admin.register(Busket)
class BusketAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'date',
    )
    list_filter = (
        ('owner', admin.BooleanFieldListFilter),
    )



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    list_filter = (
        ('name', admin.BooleanFieldListFilter),
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone_number',
        'address'
    )
    list_filter = (
        ('name', admin.BooleanFieldListFilter),
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'stock',
        'expiration_date'

    )
    list_filter = (
        ('name', admin.BooleanFieldListFilter),
    )


# Register your models here.
