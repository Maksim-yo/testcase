from django import template
from menu.models import MenuItem

register = template.Library()


def menu_items_recursion(url, items):
    if len(items) == 0:
        return
    for item in items:
        if item.url == url:
            return True
        found = menu_items_recursion(url, item.childrens.all())
        if found:
            return True
    return False
@register.inclusion_tag("menu.html")
def menu(request, menu_name):
    menu = MenuItem.objects.select_related('menu').filter(menu__name=menu_name, parent=None)
    is_active = menu_items_recursion(request.path, menu)
    return {"menu_items": menu, "request": request, 'is_active': is_active}
