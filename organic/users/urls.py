from django.urls import path

from .views import login, register, profile, logout

app_mame = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),

]