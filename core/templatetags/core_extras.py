from django import template
from django.template.defaultfilters import stringfilter
import urllib

register = template.Library()

@register.filter(name = 'decode')
@stringfilter
def decode(value):
    return value if not value else value.decode('unicode_escape')
