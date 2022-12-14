from django.db.models import Max, Min
from django.http import HttpResponseRedirect

from cart.cart import Cart
from .models import Product, Product_Category, Manufacturer


class DataMixin:
    paginate_by = 6

    def get_user_context(self, **kwargs):
        context = kwargs
        # context['extreme_prices'] = Product.objects.aggregate(Max('price'), Min('price'))
        context['brand_filter'] = self.request.GET.getlist('brand')
        context['sorted_by'] = self.request.GET.get('sort_by')
        return context

    def get_user_queryset(self, queruset):
        brand_filter = self.request.GET.getlist('brand')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        sort_by = self.request.GET.get('sort_by')
        products = queruset
        if brand_filter:
            products = products.filter(mnf_id__in=brand_filter)
        if min_price:
            products = products.filter(price__gte=float(min_price))
        if max_price:
            products = products.filter(price__lte=float(max_price))
        if sort_by:
            products = products.order_by(sort_by)
        return products
