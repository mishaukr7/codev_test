from django.contrib import admin

from catalog.models import Seller, Product


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'birthday',
    )
    list_display = fields


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = (
        'seller',
        'name',
        'description',
        'created',
        'updated',
    )
    list_display = fields
