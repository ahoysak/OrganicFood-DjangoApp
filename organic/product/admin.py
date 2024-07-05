from django.contrib import admin

from .models import Product, CountryProducingCategory, CompanyProducingCategory, ChoiceProductCategory, CompleteCart, Cart


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'id', 'photo', 'publication')
    list_display_links = ('id', 'product_name')
    search_fields = ('about', 'product_name', 'id')
    list_editable = ('publication',)
    list_filter = ('publication', )
    prepopulated_fields = {'slug': ('product_name', 'weight', 'price')}


class CompleteCartAdmin(admin.ModelAdmin):
    list_display = ('name_cart', 'price_cart', 'id', )


class AdminCart(admin.ModelAdmin):
    list_display = ('product', 'user')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    prepopulated_fields = {"company_slug": ("name", )}


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    prepopulated_fields = {"country_slug": ("name", )}


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    prepopulated_fields = {"choice_slug": ("name", )}


admin.site.register(Product, ProductAdmin)
admin.site.register(CompleteCart, CompleteCartAdmin)
admin.site.register(CountryProducingCategory, CountryAdmin)
admin.site.register(CompanyProducingCategory, CompanyAdmin)
admin.site.register(ChoiceProductCategory, ChoiceAdmin)
admin.site.register(Cart, AdminCart)
