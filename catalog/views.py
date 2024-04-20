from django.views.generic import ListView, TemplateView, DetailView

from django.shortcuts import render

from catalog.models import Product


# def home(request):
#     context = {
#         'title': 'Главная',
#         'object_list': Product.objects.all(),
#     }
#     return render(request, 'catalog/home.html', context)


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'object_list'
    extra_context = {
        'title': 'Главная',
    }


class ContactPageView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f'You have new message from {name}({phone}): {message}')
        return render(request, self.template_name)


# def product(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk),
#         'title': 'Описание продукта',
#     }
#     return render(request, 'catalog/product.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'object'
    extra_context = {
        'title': 'Описание продукта'
    }

# class ProductListView(ListView):
#     model = Product
#     extra_context = {
#         'title': 'Описание продукта',
#     }
#     template_name = 'catalog/product_list.html'

# def get_queryset(self):
#     queryset = super().get_queryset()
#     queryset = queryset.filter(product=self.kwargs.get('pk'))
#     return queryset
#
# def get_context_data(self, *args, **kwargs):
#     context_data = super().get_context_data(*args, **kwargs)
#     context_data['object'] = Product.objects.get(pk=pk)
#     return context_data
