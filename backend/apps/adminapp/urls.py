from django.urls import re_path
import backend.apps.adminapp.views as admin

app_name = 'admin'

urlpatterns = [
    re_path(r'^$', admin.index, name='index'),

    re_path(r'^user_list/$', admin.user_list, name='user_list'),
    re_path(r'^user/create/$', admin.user_create, name='user_create'),
    re_path(r'^user/update/(?P<pk>\d+)/$', admin.user_update, name='user_update'),
    re_path(r'^user/delete/(?P<pk>\d+)/$', admin.user_delete, name='user_delete'),

    re_path(r'^category/list/$', admin.productcategory_list, name='productcategory_list'),
]
