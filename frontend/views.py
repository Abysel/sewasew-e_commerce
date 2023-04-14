from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filter(category=category)
    return render(request, 'products/category.html', {'products_in_category': product, 'category': category})


def index(request):
    return render(request, 'index.html', {'products': Product.get_all_products()})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'products/detail.html', {'product': product})
