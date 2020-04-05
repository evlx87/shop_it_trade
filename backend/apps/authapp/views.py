from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from backend.apps.authapp.forms import UserLoginForm, UserRegisterForm, UserUpdateForm
from django.contrib import auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Вход в систему',
        'form': form,
    }

    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }

    return render(request, 'authapp/register.html', context)


def update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:update'))
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'page_title': 'редактирование профиля',
        'form': form
    }

    return render(request, 'authapp/update.html', context)