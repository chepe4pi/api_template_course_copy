from django.shortcuts import render

from orders.models import Order
from products.models import Product


def orders_page(request):
    return render(request, 'index.html', {'orders': Order.objects.all()})


def product_page(request):
    return render(request, 'products.html', {'products': Product.objects.all()})


def orders_page_new(request):
    return render(request, 'orders.html', {'orders': Order.objects.all()})
