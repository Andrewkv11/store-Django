from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from cart.cart import Cart
from .models import Product_Category, Product
from .forms import RegisterUserForm, LoginUserForm
from .utils import DataMixin


# Create your views here.
class MainPage(ListView):
    model = Product_Category
    template_name = 'store/index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = None
        context['new_products'] = Product.objects.order_by('-pk')[:15]
        context['discount_products'] = Product.objects.filter(discount__gt=0).order_by('-discount')
        return context


class ProductListPage(DataMixin, ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(cat_selected=0, products_for_brandlist=list(Product.objects.order_by('mnf')))
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        products = Product.objects.order_by('name')
        return self.get_user_queryset(products)


class ProductCategoryPage(DataMixin, ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(cat_selected=Product_Category.objects.get(slug=self.kwargs['slug']).pk,
                                      products_for_brandlist=list(
                                          Product.objects.filter(cat__slug=self.kwargs['slug']).order_by('mnf')))
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        products = Product.objects.filter(cat__slug=self.kwargs['slug']).order_by('name')
        return self.get_user_queryset(products)


class ProductPage(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug_product'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'store/register.html'
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'store/login.html'

    def get_success_url(self):
        return reverse_lazy('login')


def logout_user(request):
    logout(request)
    return redirect('login')


def blank_page(request):
    return render(request, 'store/blank.html')
