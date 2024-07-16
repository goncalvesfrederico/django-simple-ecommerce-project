from django.template import Library
from utils.format_price import formatprice

register = Library()

@register.filter
def priceformatted(value):
    return formatprice(value)