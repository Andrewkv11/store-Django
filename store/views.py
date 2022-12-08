from django.shortcuts import render
from .models import Product_Category, Product, Manufacturer


# Create your views here.
def main_page(request):
    categories = Product_Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'store/index.html', context=context)


def product_list_page(request):
    products = Product.objects.all()
    categories = Product_Category.objects.all()
    brands = Manufacturer.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'brands': brands,
    }
    return render(request, 'store/product_list.html', context=context)


def product_category_page(request, slug):
    products = Product.objects.filter(cat__slug=slug)
    context = {
        'products': products,
        'cat': products[0].cat
    }
    return render(request, 'store/product_category.html', context=context)


def product_page(request, slug, slug_product):
    product = Product.objects.get(slug=slug_product)
    context = {
        'product': product,
    }
    return render(request, 'store/product.html', context=context)


def checkout_page(request):
    return render(request, 'store/checkout.html')


def blank_page(request):
    return render(request, 'store/blank.html')
