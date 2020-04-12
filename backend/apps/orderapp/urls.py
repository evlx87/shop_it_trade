from django.urls import re_path
import backend.apps.orderapp.views as order

app_name = 'order'

urlpatterns = [
    re_path(r'^$', order.OrderList.as_view(), name='orders_list'),
    re_path(r'^forming/complete/(?P<pk>\d+)/$', order.order_forming_complete, name='order_forming_complete'),

    re_path(r'^create/$', order.OrderItemsCreate.as_view(), name='order_create'),
    re_path(r'^read/(?P<pk>\d+)/$', order.OrderRead.as_view(), name='order_read'),
    re_path(r'^update/(?P<pk>\d+)/$', order.OrderItemsUpdate.as_view(), name='order_update'),
    re_path(r'^delete/(?P<pk>\d+)/$', order.OrderDelete.as_view(), name='order_delete'),

]
