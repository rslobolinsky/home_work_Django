from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {
        'title': 'Главная',
        'object_list': Product.objects.all(),
    }
    return render(request, 'catalog/home.html', context)


def contact(request):
    context = {
        'title': 'Контакты',
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
        'title': 'Описание продукта',
    }
    return render(request, 'catalog/product.html', context)
