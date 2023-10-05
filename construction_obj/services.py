from django.db.models import Sum

from construction_obj.models import Section
from decimal import Decimal


def get_parent_sections(building_id: int) -> list[Section]:
    """
    Получение данных о родительских секциях объекта.
    """
    query = (Section.objects
             .filter(parent__building_id=building_id)
             .values('parent_id', 'parent__name')
             .annotate(
                    total_price=Sum('expenditure__price') * Sum('expenditure__count')
                )
             )
    return query


def get_buildings() -> list[dict]:
    """
    Получение списка объектов со стоимостью по типу.
    [
        {
            'id': 1,
            'works_amount': 100.00,
            'materials_amount': 200.00,
        },
        {
            'id': 2,
            'works_amount': 100.00,
            'materials_amount': 0.00,
        },
    ]
    """
    pass
