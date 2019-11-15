# from official docs: https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/
from django import template

register = template.Library()

# @register.filter(name="mymod")
@register.filter
def mod_by(value, arg=3):
    return bool(value % int(arg))