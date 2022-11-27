from django import template

register = template.Library()


@register.filter
def replace_slash_func(value):
    return value.replace("/", "_")
