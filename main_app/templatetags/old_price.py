from django import template


register = template.Library()


@register.filter
def old_price(value):
    return float(value) * 1.2
