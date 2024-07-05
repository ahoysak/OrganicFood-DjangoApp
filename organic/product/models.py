from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from users.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name="Ім'я Продукту")
    price = models.DecimalField(verbose_name='Ціна', max_digits=7, decimal_places=2)
    weight = models.IntegerField(verbose_name='Вага')
    about = models.TextField(verbose_name='Про товар')
    expiration_date = models.CharField(verbose_name='Термін Придатності', max_length=255)
    ingredient = models.CharField(verbose_name='Склад товару', max_length=255, null=True)
    availability = models.BooleanField(default=True, verbose_name='Наявність')
    publication = models.BooleanField(default=True, verbose_name='Публікація')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    category_country = models.ForeignKey('CountryProducingCategory', on_delete=models.PROTECT,
                                         verbose_name='Країна Виробник', default=True)
    category_company = models.ForeignKey('CompanyProducingCategory', on_delete=models.PROTECT,
                                         verbose_name='Компанія Виробник', default=True)
    category_choice = models.ForeignKey('ChoiceProductCategory', on_delete=models.PROTECT,
                                        verbose_name='Тип Продукту', default=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Органічна Продукція'
        verbose_name_plural = 'Органічна Продукція'
        ordering = ['-id']


class CompleteCart(models.Model):
    name_cart = models.CharField(max_length=255, verbose_name='Готовий набір')
    price_cart = models.DecimalField(verbose_name='Ціна', max_digits=7, decimal_places=2)
    weight_cart = models.IntegerField(verbose_name='Вага')
    about_cart = models.TextField(verbose_name='Про товар')
    photo_cart = models.ImageField(upload_to="photos/%Y/%m/%d")
    expiration_date_cart = models.CharField(verbose_name='Термін Придатності', max_length=255)
    composition_cart = models.CharField(max_length=255, verbose_name='Склад Кошика')
    country_category_cart = models.ForeignKey('CountryProducingCategory', on_delete=models.PROTECT,
                                              verbose_name='Країна Виробник')

    class Meta:
        verbose_name = 'Готовий Набір'
        verbose_name_plural = 'Готові Набори'
        ordering = ['id']


class CountryProducingCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Країна виробник')
    country_slug = models.SlugField(max_length=255, blank=True, null=True, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('country', kwargs={'country_slug': self.country_slug})

    class Meta:
        verbose_name = 'Країну Виробник'
        verbose_name_plural = 'Країни Виробник'
        ordering = ['id']


class CompanyProducingCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Компанія виробник')
    company_slug = models.SlugField(max_length=255, blank=True, null=True, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company', kwargs={'company_slug': self.company_slug})

    class Meta:
        verbose_name = 'Компанію Виробник'
        verbose_name_plural = 'Компанії Виробники'
        ordering = ['id']


class ChoiceProductCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Продукт')
    choice_slug = models.SlugField(max_length=255, blank=True, null=True, unique=True, db_index=True,
                    verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('choice', kwargs={'choice_slug': self.choice_slug})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Тип Продукту'
        ordering = ['id']


class CartQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(cart.sum() for cart in self)

    def total_quantity(self):
        return sum(cart.quantity for cart in self)


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartQuerySet.as_manager()

    def __str__(self):
        return f'Корзина Для {self.user.username} | Продукт {self.product.product_name}'

    def sum(self):
        return self.product.price * self.quantity

    class Meta:
        verbose_name = 'Кошик Користувача'
        verbose_name_plural = 'Кошик'
        ordering = ['id']
