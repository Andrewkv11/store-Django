from django.shortcuts import render
from .models import Product_Category, Product, Manufacturer


# Create your views here.
def main_page(request):
    # product_categories = Product_Category.objects.all()
    # print(product_categories)
    # context = {
    #     'product_categories': product_categories
    # }
    return render(request, 'store/index.html')


def product_page(request):
    return render(request, 'store/product.html')


def product_list_page(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/product_list.html', context=context)


def checkout_page(request):
    return render(request, 'store/checkout.html')


def blank_page(request):
    return render(request, 'store/blank.html')
