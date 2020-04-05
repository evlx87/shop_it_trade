from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from backend.apps.adminapp.forms import UserAdminCreateForm, UserAdminUpdateForm
from backend.apps.authapp.models import User
from backend.apps.mainapp.models import ProductCategory


def index(request):
    object_list = User.objects.all()[:3]

    context = {
        'page_title': 'Админка/пользователи',
        'object_list': object_list
    }
    return render(request, 'adminapp/user_list.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_create(request):
    if request.method == 'POST':
        form = UserAdminCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_panel:index'))
    else:
        form = UserAdminCreateForm()

    context = {
        'page_title': 'Админка/новый пользователь',
        'form': form
    }
    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserAdminUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_panel:index'))
    else:
        form = UserAdminUpdateForm(instance=user)

    context = {
        'page_title': 'Админка/редактирование пользователя',
        'form': form
    }
    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin_panel:index'))
    elif request.method == 'GET':
        context = {
            'page_title': 'Админка/удаление пользователя',
            'object': user,
        }
        return render(request, 'adminapp/user_delete.html', context)


@user_passes_test(lambda x: x.is_superuser)
def productcategory_list(request):
    object_list = ProductCategory.objects.all()

    context = {
        'page_title': 'Админка/категории',
        'object_list': object_list,
    }

    return render(request, 'adminapp/productcategory_list.html', context)
