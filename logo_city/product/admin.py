from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # отоброжение полей
    list_display = (
        "product",
        "created_at",
        "updated_at",
        "sale",
        "price",
        "is_active",
    )

    list_display_links = (
        "sale",
        "product",
    )
# строка поиска
    search_fields = (
        "product",
    )

    list_editable = (
        "is_active",
        "price",
    )
# фильтрация статьи списка
    list_filter = (
        "is_active",
    )


admin.site.register(Category)