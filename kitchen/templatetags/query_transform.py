from typing import Any

from django import template

from kitchen.models import Dish

register = template.Library()


@register.simple_tag
def query_transform(request, **kwargs) -> str:
    updated = request.GET.copy()
    for key, value in kwargs.items():
        if value is not None:
            updated[key] = value
        else:
            updated.pop(key, 0)

    return updated. urlencode()


@register.simple_tag
def get_dishes_of_type(dish_type: str) -> Any:
    return Dish.objects.filter(dish_type__name=dish_type)