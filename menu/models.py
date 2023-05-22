from django.db import models


class Product(models.Model):
    name = models.CharField( verbose_name='Название', max_length = 50)
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField(verbose_name="Фото товара", upload_to="products")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'