from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from .models import Product, CompleteCart, Cart
from .utils import DataMixin
from users.models import User

from users.forms import UserProfileForm, UserLoginForm


class ProductHomeView(ListView):
    paginate_by = 8
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(publication=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Organic Food'
        return context


class ProductShopView(DataMixin, ListView):
    models = Product
    template_name = 'product/shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(publication=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        class_mixin = self.get_user_context(title='Organic Food | Продукти')
        return dict(list(context.items()) + list(class_mixin.items()))


class ShopCategoryView(DataMixin, ListView):
    model = Product
    template_name = 'product/shop.html'
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(category_choice__choice_slug=self.kwargs['choice_slug'], publication=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        class_mixin = self.get_user_context(title='Organic Food | ' +
                                            str(context['products'][0].category_choice),
                                            category_choice_selected=context['products'][0].category_choice_id)

        return dict(list(context.items()) + list(class_mixin.items()))


class ShowProductPostView(DataMixin, DetailView):
    model = Product
    template_name = 'product/product.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        class_mixin = self.get_user_context(title='Organic Food | ' + str(context['posts'].product_name))
        return dict(list(context.items()) + list(class_mixin.items()))


class CompleteCartView(DataMixin, ListView):
    model = CompleteCart
    template_name = 'product/product-single.html'
    context_object_name = 'cart_component'

    def get_queryset(self):
        return CompleteCart.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        class_mixin = self.get_user_context(title='Organic Food | Готовий набір')

        return dict(list(context.items()) + list(class_mixin.items()))


@login_required
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    carts = Cart.objects.filter(user=request.user, product=product)

    if not carts.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def cart_remove(request, product_id):
    cart = Cart.objects.get(id=product_id)
    cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def remove_all_cart(request):
    cart = Cart.objects.all()
    cart.delete()

    return HttpResponseRedirect('/')


def confirm_order(request):
    form = UserProfileForm(instance=request.user)

    context = {'title': 'Organic Food | Підтвердження Замовлення', 'form': form}
    return render(request, 'product/confirm_order.html', context)


def about(request):
    context = {'title': 'Organic Food | Про нас'}
    return render(request, 'product/about.html', context)


def police(request):
    context = {'title': 'Organic Food | FAQ'}
    return render(request, 'product/privacy_police.html', context)


def pageNotFound(request, exception):
    return render(request, 'product/notFound.html', status=404)


