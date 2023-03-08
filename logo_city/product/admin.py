from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "created_at",
        "updated_at",
        "sale",
        "price",
    )
