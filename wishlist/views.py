from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .wishlist import Wishlist


# Create your views here.
@require_POST
def change_wishlist(request, product_id):
    wishlist = Wishlist(request)
    wishlist.change_wishlist(product_id)
    return redirect(request.POST['redirect_url'])


def view_wishlist(request):
    return render(request, 'wishlist/wishlist.html')
