from django.shortcuts import render

from orders.models import Order


def orders_page(request):
    return render(request, 'index.html', {'orders': Order.objects.all()})
