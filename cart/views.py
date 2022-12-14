from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from django.views.decorators.http import require_POST
from store.models import Product


# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = request.POST.get('quantity')
    cart.add(product=product, quantity=quantity)
    return redirect(request.POST['redirect_url'])


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove_elem(product)
    return redirect(request.POST['redirect_url'])
