from django.urls import path

from catalog.views import home, contact

urlpatterns = [
    path('', home, name='home'),
    # path('category/', category_list, name='category'),
    # path('<int:pk>_category/', category_product, name='category_product'),
    # path('<int:pk>_product/', product, name='product'),
    path('contacts/', contact, name='contacts')
    ]