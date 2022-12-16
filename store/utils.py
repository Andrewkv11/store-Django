from django.contrib.postgres.search import SearchVector
from .forms import SearchForm

class DataMixin:
    paginate_by = 6

    def get_user_context(self, **kwargs):
        context = kwargs
        # context['extreme_prices'] = Product.objects.aggregate(Max('price'), Min('price'))
        context['brand_filter'] = self.request.GET.getlist('brand')
        context['sorted_by'] = self.request.GET.get('sort_by')
        if self.request.GET.get('search'):
            context['search_form'] = SearchForm(self.request.GET)
        else:
            context['search_form'] = SearchForm()
        return context

    def get_user_queryset(self, queruset):
        brand_filter = self.request.GET.getlist('brand')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        sort_by = self.request.GET.get('sort_by')
        search = self.request.GET.get('search')
        products = queruset
        if brand_filter:
            products = products.filter(mnf_id__in=brand_filter)
        if min_price:
            products = products.filter(price__gte=float(min_price))
        if max_price:
            products = products.filter(price__lte=float(max_price))
        if sort_by:
            products = products.order_by(sort_by)
        if search:
            form = SearchForm(self.request.GET)
            if form.is_valid():
                search = form.cleaned_data['search']
                products = products.annotate(search=SearchVector('name')).filter(search=search)
        return products
