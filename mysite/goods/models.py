from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название категории товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товара'
        ordering = ('name',)


class Product(models.Model):
    vendor_code = models.IntegerField(verbose_name='Артикул')
    name = models.CharField(max_length=128, verbose_name='Название товара')
    price = models.PositiveIntegerField(verbose_name='Цена товара')
    description = models.TextField(max_length=512, verbose_name='Описание товара', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
