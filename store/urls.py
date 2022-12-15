from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('all/', ProductListPage.as_view(), name='product_list_page'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('blank/', blank_page, name='blank'),
    path('<slug:slug>/', ProductCategoryPage.as_view(), name='product_category_page'),
    path('<slug:slug>/<slug:slug_product>/', ProductPage.as_view(), name='product_page'),
]
