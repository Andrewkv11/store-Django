from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('all/', product_list_page, name='product_list_page'),
    path('c/', checkout_page, name='checkout_page'),
    path('b/', blank_page, name='blank_page'),
    path('<slug:slug>/', product_category_page, name='product_category_page'),
    path('<slug:slug>/<slug:slug_product>/', product_page, name='product_page'),
]
