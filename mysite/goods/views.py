from django.http import Http404

from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.shortcuts import render, redirect, get_object_or_404


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()
        context = {
            'form': form
        }
        return render(request, 'create_product.html', context)


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CategoryForm()
        context = {
            'form': form
        }
        return render(request, 'create_category.html', context)


def product_view(request):
    dataset_products = Product.objects.all()
    dataset_categories = Category.objects.all()
    return render(request, 'list_view.html', {
        'dataset_products': dataset_products,
        'dataset_categories': dataset_categories,
    })


def product_detail_view(request, id):
    try:
        data = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404('Товар не найден')

    return render(request, 'detail_view.html', {'data': data})


def update_product(request, id):
    try:
        old_data = get_object_or_404(Product, id=id)
    except Exception:
        raise Http404('Товар не найден')
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect(f'/{id}')
    else:
        form = ProductForm(instance=old_data)
        context = {
            'form': form
        }
        return render(request, 'update_product.html', context)


def delete_product(request, id):
    try:
        data = get_object_or_404(Product, id=id)
    except Exception:
        raise Http404('Товар не найден')

    if request.method == 'POST':
        data.delete()
        return redirect('/')
    else:
        return render(request, 'delete_product.html', {'data': data})
