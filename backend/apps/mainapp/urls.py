from django.urls import re_path
import backend.apps.mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.main, name='index'),
    re_path(r'^catalog/$', mainapp.catalog, name='catalog'),
    re_path(r'^contacts/$', mainapp.contacts, name='contacts'),
]
