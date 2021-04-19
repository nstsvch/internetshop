from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import Product


def home_page(request):
    return render(request, 'main/base.html')


def show_all(request):
    products = Product.objects.all()
    return render(request, 'main/collection.html', {'products': products})


def login(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = RegistrationForm()
    return render(request, 'main/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})