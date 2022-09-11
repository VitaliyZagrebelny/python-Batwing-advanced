from django import template
from main.models import MenuItem


register = template.Library()

@register.inclusion_tag("main/menu_item.html")
def menu():
    return {"menu_list": MenuItem.objects.all()}