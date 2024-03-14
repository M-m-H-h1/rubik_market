from django import template
import os
import re
register = template.Library()

@register.filter
def order_bya(value,arg):
    return value.order_by(arg)

@register.filter
def price_format(price):
    return '{:,.0f}'.format(price)


@register.filter
def split_by_space(value):
    if value:
        return value.split(' ', 1)[0]
    return value



@register.filter()
def get_list(dictionary, key):
    return dictionary.getlist(key)





@register.filter
def remove_param(value, param_name):
    params = value.copy()
    if param_name in params:
        del params[param_name]
    return params.urlencode()





@register.filter
def add_param(value, param):
    params = value.copy()
    key, val = param.split('=')
    params[key] = val
    return params.urlencode()


@register.filter
def intcomma(value):
    orig = str(value)
    new = ""
    while orig != new:
        orig = new if new else orig
        new = re.sub(r"^(-?\d+)(\d{3})", r"\1,\2", orig)
    return new



@register.filter
def extract_filename(value):
    return os.path.basename(value)