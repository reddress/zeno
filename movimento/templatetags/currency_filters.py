from django import template

register = template.Library()


@register.filter(needs_autoescape=True)
def currencyCents(value, autoescape=True):
    return "$ {:,.2f}".format(value / 100.0).translate(str.maketrans(",.", ".,"))
