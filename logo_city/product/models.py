from django.db import models


class Product(models.Model):
    product = models.CharField(
        verbose_name="Название товара",
        max_length=100
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

    def __str__(self):
        return self.product
