from django.db.models import Q
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
            'form': form,
            'title': 'Добавить товар'
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
            'form': form,
            'title': 'Добавить категорию товара'
        }
        return render(request, 'create_category.html', context)


def category_view(request):
    dataset_categories = Category.objects.all()
    context = {
        'dataset_categories': dataset_categories,
        'title': 'Список категорий товаров'
    }
    return render(request, 'list_view.html', context)


def product_detail_view(request, id):
    try:
        data = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404('Товар не найден')
    context = {
        'data': data,
    }
    return render(request, 'detail_view.html', context)


def category_detail_view(request, id):
    try:
        category = Category.objects.get(id=id)
        data = Product.objects.filter(category=id)
    except Category.DoesNotExist:
        raise Http404('Категория товара не найдена')
    context = {
        'data': data,
        'category': category
    }
    return render (request, 'category_view.html', context)


def update_product(request, id):
    try:
        old_data = get_object_or_404(Product, id=id)
    except Exception:
        raise Http404('Товар не найден')
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect(f'/product/{id}')
    else:
        form = ProductForm(instance=old_data)
        context = {
            'form': form,
            'title': 'Обновить товар'
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


def search_results(request):
    query = request.GET.get('q')
    if query is None:
        data = Product.objects.all()
    else:
        data = Product.objects.filter(
            Q(vendor_code__icontains=query) |
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query))
    context = {
        'title': 'Результат поиска',
        'data': data
    }
    return render(request, 'search.html', context)
