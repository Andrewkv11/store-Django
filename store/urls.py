from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('p/', product_list_page, name='product_list_page'),
    path('s/', product_page, name='product_page'),
    path('c/', checkout_page, name='checkout_page'),
    path('b/', blank_page, name='blank_page'),
]
