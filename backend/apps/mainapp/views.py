import json
from django.shortcuts import render, get_object_or_404

from backend.apps.mainapp.models import Product, ProductCategory


# Create your views here.
def get_products_menu():
    return ProductCategory.objects.all()


def get_basket(request):
    if request.user.is_authenticated:
        return request.user.basket.all().order_by('product__category')
    else:
        return []


def main(request):
    new_products = Product.objects.all()

    context = {
        'page_title': 'Магазин',
        'new_products': new_products
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    catalog_products = Product.objects.all()[:8]

    context = {
        'page_title': 'Каталог',
        'products_menu': get_products_menu(),
        'catalog_products': catalog_products,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/catalog.html', context)


def contacts(request):
    context = {
        'page_title': 'Контакты',
    }
    return render(request, 'mainapp/contacts.html', context)


def product(request, pk):
    context = {
        'page_title': 'Страница товара',
        'product': get_object_or_404(Product, pk=pk),
        'products_menu': get_products_menu(),
        'category': Product.category,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/product.html', context)