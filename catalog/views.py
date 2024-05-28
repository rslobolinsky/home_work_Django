from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version, Category
from catalog.services import get_products_from_cache, get_categories_from_cache


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        products = context_data['object_list']

        for product in products:
            versions = Version.objects.filter(product=product, is_current=True)
            if versions:
                product.version = versions.last()
        context_data['object_list'] = products
        return context_data

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Описание продукта'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        active_version = self.object.version_set.filter(is_current=True).first()
        if active_version:
            context_data['version'] = active_version
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        product_formset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = product_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = product_formset(instance=self.object)

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if (user.has_perm('catalog.can_edit_category') and user.has_perm('catalog.can_edit_description')
                and user.has_perm('catalog.can_change_published')):
            return ProductModeratorForm
        if user == self.object.owner:
            return ProductForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    login_url = '/users/register/'

    def get_queryset(self):
        return get_categories_from_cache()


class ContactsPageView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f'{name} ({phone}): {message}')
        return render(request, 'catalog/contacts.html', context=self.extra_context)
