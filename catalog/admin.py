from datetime import datetime, timedelta

from django.contrib import admin

from catalog.models import Seller, Product

DATE_RANGE = (
    (1, 'Last 1 day'),
    (3, 'Last 3 days'),
    (7, 'Last 7 days'),
)


class ProductByCreatedFilter(admin.SimpleListFilter):
    title = 'created'
    parameter_name = 'created'

    def lookups(self, request, model_admin):
        return DATE_RANGE

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(created__gte=datetime.now()-timedelta(days=int(value)))
        return queryset


class ProductByUpdatedFilter(admin.SimpleListFilter):
    title = 'updated'
    parameter_name = 'updated'

    def lookups(self, request, model_admin):
        return DATE_RANGE

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(updated__gte=datetime.now()-timedelta(days=int(value)))
        return queryset


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
    readonly_fields = (
        'created',
        'updated',
    )
    list_display = fields
    list_filter = (ProductByCreatedFilter, ProductByUpdatedFilter, )

