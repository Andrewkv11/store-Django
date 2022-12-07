from django import template
from store.models import *

register = template.Library()


@register.simple_tag()
def get_product_categories():
    return Product_Category.objects.all()
