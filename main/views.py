from django.shortcuts import render

from main.models import Product


def show_all(request):
    products = Product.objects.all()
    return render(request, 'main/collection.html', {'products': products})