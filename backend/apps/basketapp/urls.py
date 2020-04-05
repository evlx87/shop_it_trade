from django.urls import re_path
import backend.apps.basketapp.views as basket

app_name = 'basket'

urlpatterns = [
    re_path(r'^$', basket.index, name='index'),
    re_path(r'add/(?P<pk>\d+)/', basket.basket_add, name='add'),
    re_path(r'delete/(?P<pk>\d+)/', basket.basket_delete, name='delete'),
]
