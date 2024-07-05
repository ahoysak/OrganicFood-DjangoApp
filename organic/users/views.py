from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import UserLoginForm, RegisterUserForm, UserProfileForm
from product.models import Cart


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вітаємо,реєстрація успішна!')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegisterUserForm()

    context = {'form': form, 'title': 'Organic Food | Реєстрація'}
    return render(request, 'users/register.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    context = {'form': form, 'title': 'Organic Food | Вхід'}

    return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile(request):
    form = UserProfileForm(instance=request.user)

    context = {'form': form,
               'title': 'Особистий кабінет',
               'carts':  Cart.objects.filter(user=request.user),
               }

    return render(request, 'users/profile.html', context)
