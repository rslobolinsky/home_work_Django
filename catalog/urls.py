from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactPageView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name
urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('contacts/', ContactPageView.as_view()),
    path('product/create', ProductCreateView.as_view(), name='create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
]
