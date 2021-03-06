from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=128, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активность', default=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='prod_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание товара', max_length=64)
    description = models.TextField(verbose_name='описание товара', blank=True)
    price = models.DecimalField(verbose_name='цена товара', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
