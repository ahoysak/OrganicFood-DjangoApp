# Generated by Django 5.0.2 on 2024-02-22 10:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='completecart',
            name='country_category_cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.countryproducingcategory', verbose_name='Країна Виробник'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_choice',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='product.choiceproductcategory', verbose_name='Тип Продукту'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_company',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='product.companyproducingcategory', verbose_name='Компанія Виробник'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_country',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='product.countryproducingcategory', verbose_name='Країна Виробник'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]