"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from goods.views import create_product, create_category, product_view, product_detail_view, update_product, \
    delete_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_product/', create_product),
    path('create_category/', create_category),
    path('category/<int:id>/', category_detail_view),
    path('', category_view),
    path('product/<int:id>/', product_detail_view),
    path('update/<int:id>/', update_product),
    path('delete/<int:id>/', delete_product),
]
