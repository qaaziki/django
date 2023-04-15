from django.db import models


class Product(models.Model):
    product = models.CharField(
        verbose_name="Название товара",
        max_length=255
    )
    is_active = models.BooleanField(
        verbose_name="Показывать товар",
        default=False
    )
    description = models.TextField(
        verbose_name="Описание товара",
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now=True
    )
    sale = models.IntegerField(
        verbose_name="Процент скидки",
        default=0
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2,
    )

    category = models.ForeignKey(
        "Category", verbose_name="Категория",
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to="products_image",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.product


class Category(models.Model):
    title = models.CharField(
        verbose_name="Название категории",
        max_length=255,

    )

    def __str__(self):
        return self.title
