from django import template

register = template.Library()


@register.filter()
def my_tags(path):
    if path:
        return f'/media/{path}'
    return "#" # default