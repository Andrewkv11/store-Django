from django.urls import path
from .views import *

urlpatterns = [
    path('view_wishlist/', view_wishlist, name='view_wishlist'),
    path('change_wishlist/<int:product_id>/', change_wishlist, name='change_wishlist'),
]