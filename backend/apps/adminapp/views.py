from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from backend.apps.adminapp.forms import UserAdminCreateForm, UserAdminUpdateForm, ProductCategoryAdminUpdateForm, \
    ProductAdminUpdateForm
from backend.apps.authapp.models import User
from backend.apps.mainapp.models import ProductCategory, Product


def index(request):
    context = {
        'page_title': 'Админка',
    }
    return render(request, 'adminapp/admin_panel.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_list(request):
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
def category_list(request):
    object_list = ProductCategory.objects.all()

    context = {
        'page_title': 'Админка/категории',
        'object_list': object_list,
    }

    return render(request, 'adminapp/category_list.html', context)


class CategoryCreateView(CreateView):
    model = ProductCategory
    success_url = reverse_lazy('admin_panel:category_list')
    form_class = ProductCategoryAdminUpdateForm


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    success_url = reverse_lazy('admin_panel:category_list')
    form_class = ProductCategoryAdminUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Админка/редактирование категории товара'
        return context


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('admin_panel:category_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda x: x.is_superuser)
def category_products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)

    context = {
        'page_title': 'Админка/товары категории',
        'category': category,
        'object_list': category.product_set.all()
    }

    return render(request, 'adminapp/product_list.html', context)


@user_passes_test(lambda x: x.is_superuser)
def product_create(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductAdminUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_panel:category_products', kwargs={'pk': pk}))
    else:
        form = ProductAdminUpdateForm(initial={'category': category})

    context = {
        'page_title': 'Админка/новый товар',
        'form': form,
    }

    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductAdminUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_panel:category_products', kwargs={'pk': product.category.pk}))
    else:
        form = ProductAdminUpdateForm(instance=product)

    context = {
        'page_title': 'Админка/редактирование товара',
        'form': form,
        'object': product
    }

    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin_panel:category_products', kwargs={'pk': product.category.pk}))
    elif request.method == 'GET':
        context = {
            'page_title': 'Админка/удаление продукта',
            'object': product,
        }
        return render(request, 'adminapp/product_delete.html', context)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Админка/Подробная информация'
        return context
