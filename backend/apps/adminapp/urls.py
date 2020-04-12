from django.urls import re_path
import backend.apps.adminapp.views as admin

app_name = 'admin'

urlpatterns = [
    re_path(r'^$', admin.index, name='index'),

    re_path(r'^user_list/$', admin.user_list, name='user_list'),
    re_path(r'^user/create/$', admin.user_create, name='user_create'),
    re_path(r'^user/update/(?P<pk>\d+)/$', admin.user_update, name='user_update'),
    re_path(r'^user/delete/(?P<pk>\d+)/$', admin.user_delete, name='user_delete'),

    re_path(r'^category/list/$', admin.category_list, name='category_list'),
    re_path(r'^category/create/$', admin.CategoryCreateView.as_view(), name='category_create'),
    re_path(r'^category/update/(?P<pk>\d+)/$', admin.CategoryUpdateView.as_view(), name='category_update'),
    re_path(r'^category/delete/(?P<pk>\d+)/$', admin.CategoryDeleteView.as_view(), name='category_delete'),
    re_path(r'^category/products/(?P<pk>\d+)/$', admin.category_products, name='category_products'),

    re_path(r'^product/create/(?P<pk>\d+)/$', admin.product_create, name='product_create'),
    re_path(r'^product/read/(?P<pk>\d+)/$', admin.ProductDetailView.as_view(), name='product_read'),
    re_path(r'^product/update/(?P<pk>\d+)/$', admin.product_update, name='product_update'),
    re_path(r'^product/delete/(?P<pk>\d+)/$', admin.product_delete, name='product_delete'),
]
