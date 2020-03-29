import json
from django.shortcuts import render
from backend.apps.mainapp.models import Product, ProductCategory


# Create your views here.
def main(request):
    new_products = Product.objects.all()

    context = {
        'page_title': 'магазин',
        'new_products': new_products
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    product = [
        {
            'name': 'Неуправляемый коммутатор DES-1016D с 16 портами 10/100Base-TX',
            'img': '/static/img/dlink.jpg',
            'link': '#'
        },
        {
            'name': 'Маршрутизатор TP-LINK TL-R470T+',
            'img': '/static/img/tplink.jpg',
            'link': '#'
        },
        {
            'name': 'Сетевое хранилище Zyxel NAS326',
            'img': '/static/img/zyxel.jpg',
            'link': '#'
        },
    ]

    with open('backend/json/products.json', 'w', encoding='utf-8') as f:
        json.dump(product, f)

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
