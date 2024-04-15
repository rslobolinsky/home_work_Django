from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contact, product

app_name = CatalogConfig.name
urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>', product, name='product'),
    path('contacts/', contact, name='contacts')
]
