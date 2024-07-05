from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductHomeView.as_view(), name='home'),
    path('about', about, name='about'),
    path('shop', ProductShopView.as_view(), name='shop'),
    path('privacy-police', police, name='police'),
    path('complete_cart', CompleteCartView.as_view(), name='complete_cart'),
    path('product/<slug:choice_slug>/', ShopCategoryView.as_view(), name='choice'),
    path('food/<slug:post_slug>/', ShowProductPostView.as_view(), name='post'),
    path('cart/add/<int:product_id>/', add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('confirm-order', confirm_order, name='confirm'),
    path('confirm-order2', remove_all_cart, name='removee')

]
