from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(value, num):
    return value * num
