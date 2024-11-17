from django import template

register = template.Library()

@register.filter
def range_filter(value):
    if value > 5: value = 5
    return range(value)
