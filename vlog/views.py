from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from vlog.models import Vlog


class VlogListView(ListView):
    model = Vlog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class VlogDetailView(DetailView):
    model = Vlog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class VlogCreateView(CreateView):
    model = Vlog
    fields = ('name', 'text', 'preview', 'is_published')
    success_url = reverse_lazy('vlog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.name)
            new_art.save()
        return super().form_valid(form)


class VlogUpdateView(UpdateView):
    model = Vlog
    fields = ('name', 'text', 'preview', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.name)
            new_art.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('vlog:view', args=[self.kwargs.get('pk')])


class VlogDeleteView(DeleteView):
    model = Vlog
    success_url = reverse_lazy('vlog:list')
