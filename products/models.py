from django.db import models


class Size(models.Model):
    size = models.CharField(max_length=20, verbose_name='Размер')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размер'

    def __str__(self):
        return self.size


class Categories(models.Model):
    categories = models.CharField(max_length=20, verbose_name='Категории')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.categories


class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    size = models.ForeignKey(Size, null=True, blank=True, verbose_name='Размер', on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, verbose_name='Категории', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    slivki = models.BooleanField(verbose_name='Наличие на сливках', default=False)
    price_sliv = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена на сливках', null=True, blank=True)
    discount = models.BooleanField(default=True, verbose_name='Действует скидка')


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return self.name
