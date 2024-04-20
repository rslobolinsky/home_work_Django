from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactPageView, ProductDetailView

app_name = CatalogConfig.name
urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('contacts/', ContactPageView.as_view())
]
