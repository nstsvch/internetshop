from django.shortcuts import render
from orders.models import Order


def orders_page(request):
    return render(request, 'main/base.html', {'orders': Order.objects.all()})


def login(request):
    return render(request, 'login.html')
