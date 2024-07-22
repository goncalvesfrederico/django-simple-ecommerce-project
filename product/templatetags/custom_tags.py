from django.template import Library
from utils.format_price import formatprice
from utils.utils import qty_items, cart_total

register = Library()

@register.filter
def priceformatted(value):
    return formatprice(value)

@register.filter
def total_number_items_cart(value):
    return qty_items(value)

@register.filter
def sum_total_value_cart(value):
    return cart_total(value)