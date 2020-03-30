from django.urls import re_path
import backend.apps.authapp.views as auth

app_name = 'auth'

urlpatterns = [
    re_path(r'^login/$', auth.login, name='login'),
    re_path(r'^logout/$', auth.logout, name='logout'),
    re_path(r'^register/$', auth.register, name='register'),
    re_path(r'^update/$', auth.update, name='update'),
]
