from .models import Product, Category
from django.forms import ModelForm


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ('vendor_code', 'name', 'price', 'description', 'category')


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ('name',)
