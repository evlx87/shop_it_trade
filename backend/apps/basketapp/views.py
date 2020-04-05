from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from backend.apps.mainapp.views import get_basket
from backend.apps.basketapp.models import Basket
from backend.apps.mainapp.models import Product


@login_required
def index(request):
    context = {
        'page_title': 'Корзина',
        'basket': get_basket(request),
    }
    return render(request, 'basketapp/basket.html', context)


@login_required
def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_item = Basket.objects.filter(user=request.user,
                                        product=product).first()
    if basket_item:
        basket_item.quantity += 1
        basket_item.save()
    else:
        Basket.objects.create(user=request.user,
                              product=product,
                              quantity=1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_delete(request, pk):
    get_object_or_404(Basket, pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
