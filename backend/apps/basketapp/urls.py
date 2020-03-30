from django.urls import re_path
import backend.apps.basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    re_path(r'^$', basketapp.index, name='index'),
    re_path(r'add/(?P<pk>\d+)/', basketapp.basket_add, name='add'),
]
