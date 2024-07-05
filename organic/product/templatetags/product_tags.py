from django import template
from product.models import ChoiceProductCategory

register = template.Library()


@register.simple_tag()
def get_category():
    return ChoiceProductCategory.objects.all()

