from django.contrib import admin
from main.models import *
# Register your models here.

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category',)
    fields = ('image', 'name', 'description',('price', 'quantity'), 'category',)
    # exclude = ['stripe_product_price_id']
    # readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('-name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp',)
    readonly_fields = ('created_timestamp',)
    extra = 0
    
