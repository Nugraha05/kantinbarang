"""cateringbekasi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from product import views as productView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', productView.makanan, name='makanan'),
    path('minuman/', productView.minuman, name='minuman'),
    path('makanan/<int:data_id>', productView.detail, name='detail'),
    path('pesanan/', productView.view_cart, name='pesanan'),
    path('add_to_cart/<int:data_id>/', productView.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:data_id>/', productView.remove_from_cart, name='remove_from_cart')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
