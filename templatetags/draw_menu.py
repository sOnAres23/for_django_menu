from django import template
from app.models import MenuCase

register = template.Library()


def get_active_items(items, active_url):
    """Получение активных пунктов"""
    active_items = []
    for item in items:
        if item.url == active_url or active_url.startswith(item.url):
            active_items.append(item)
            active_items.extend(get_active_items(item.children.all(), active_url))
    return active_items


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    active_url = request.path

    # Получаем все пункты меню по имени
    items = MenuCase.objects.filter(menu_name=menu_name).select_related('parent')

    # Определяем активные пункты
    active_items = get_active_items(items, active_url)

    return {
        'items': items,
        'active_items': active_items,
        'active_url': active_url,
    }
