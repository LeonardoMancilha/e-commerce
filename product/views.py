from django.shortcuts import render


def view_products(request):
    return render(request, 'product/products.html')
