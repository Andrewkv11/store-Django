from django import template
from store.models import *

register = template.Library()


@register.filter(name='str')
def int_to_str(value):
    return str(value)


@register.simple_tag()
def get_product_categories():
    return Product_Category.objects.all()
