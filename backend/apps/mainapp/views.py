import json
from django.shortcuts import render
from backend.apps.mainapp.models import Product, ProductCategory


# Create your views here.
def get_basket(request):
    if request.is_authenticated:
        return request.basket.all().order_by('product__category')
    else:
        return []


def main(request):
    new_products = Product.objects.all()

    context = {
        'page_title': 'магазин',
        'new_products': new_products
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    with open('backend/json/products.json', 'r', encoding='utf-8') as f:
        product = json.load(f)

    context = {
        'page_title': 'каталог',
        'product': product,
    }
    return render(request, 'mainapp/catalog.html', context)


def contacts(request):
    context = {
        'page_title': 'контакты',
    }
    return render(request, 'mainapp/contacts.html', context)
