from django.contrib.auth.forms import UserCreationForm

from .forms import RegistrationForm, UserLoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import Product
from django.contrib.auth import login, logout


def home_page(request):
    return render(request, 'main/base.html')


def show_all(request):
    products = Product.objects.all()
    return render(request, 'main/collection.html', {'products': products})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('/')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})


