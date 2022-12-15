from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.cart import Cart
from .forms import OrderCreateForm


# Create your views here.
def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = Order(
                username=request.user,
                city=form.cleaned_data['city'],
                address=form.cleaned_data['address'],
            )
            order.save()
            for item in cart.cart_elem():
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return redirect('created_order')
    else:
        form = OrderCreateForm()
    return render(request, 'order/create_order.html', context={'form': form})


def created_order(request):
    orders = Order.objects.filter(username=request.user)
    return render(request, 'order/created_order.html', context={'orders': orders})
