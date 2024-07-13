from django import template

register = template.Library()


@register.filter()
def catalog_filter(path):
    if path:
        return f'/media/{path}'
    return "#" # default