from django.contrib import admin
# Import count object
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html

from . import models


# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'unit_price', 'inventory_status', 'collection')
    search_fields = ('title', 'description', 'unit_price')
    ordering = ('title', 'unit_price')
    list_editable = ('unit_price', )
    list_filter = ('collection', 'last_update')
    list_per_page = 30

    @admin.display(ordering='inventory')
    def inventory_status(self, obj):
        return 'In stock' if obj.inventory > 0 else 'Out of stock'


# admin.site.register(models.Collection)
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'products_count',)
    list_per_page = 10

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = reverse('admin:store_product_changelist') + \
            '?collection__id=%d' % collection.id
        return format_html('<a href="{}">{}</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count('product'))


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',
                    'phone', 'birth_date', 'membership', 'orders_count')
    search_fields = ('first_name', 'last_name', 'email',
                     'phone', 'birth_date', 'membership')
    ordering = ('first_name', 'last_name', 'email',
                'phone', 'birth_date', 'membership')
    list_editable = ('membership',)
    # number of rows to display per page
    list_per_page = 25
    @admin.display(ordering='orders_count')
    def orders_count(self, customer):
        url = reverse('admin:store_order_changelist') + \
            '?customer__id=%d' % customer.id
        return format_html('<a href="{}">{}</a>', url, customer.orders_count)
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(orders_count=Count('order'))


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'payment_status', 'placed_at')
    list_per_page = 25
