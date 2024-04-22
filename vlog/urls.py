"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from vlog.apps import VlogConfig
from vlog.views import VlogListView, VlogDetailView, VlogCreateView, VlogUpdateView, VlogDeleteView

app_name = VlogConfig.name

urlpatterns = [
    path('', VlogListView.as_view(), name='list'),
    path('view/<int:pk>', VlogDetailView.as_view(), name='view'),
    path('create/', VlogCreateView.as_view(), name='create'),
    path('edit/<int:pk>', VlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', VlogDeleteView.as_view(), name='delete')
]

