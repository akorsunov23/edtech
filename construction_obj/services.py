from django.db import models
from django.db.models import Sum

from construction_obj.models import Section, Building, Expenditure
from decimal import Decimal


def get_parent_sections(building_id: int) -> list[Section]:
    """
    Получение данных о родительских секциях объекта.
    """
    query = (
        Section.objects.filter(parent__building_id=building_id)
        .values(
            "parent_id",
            "parent__name"
        )
        .annotate(
            total_price=Sum("expenditure__price")
            * Sum("expenditure__count")
        )

    )
    return query


def get_buildings() -> list[dict]:
    """
    Получение списка объектов со стоимостью по типу.
    """
    query = (
        Building.objects.all()
        .annotate(
            works_amount=Sum(
                "section__expenditure__price",
                filter=models.Q(
                    section__expenditure__type=Expenditure.Types.WORK
                ),
            )
            * Sum(
                "section__expenditure__count",
                filter=models.Q(
                    section__expenditure__type=Expenditure.Types.WORK
                ),
            ),
            materials_amount=Sum(
                "section__expenditure__price",
                filter=models.Q(
                    section__expenditure__type=Expenditure.Types.MATERIAL
                ),
            )
            * Sum(
                "section__expenditure__count",
                filter=models.Q(
                    section__expenditure__type=Expenditure.Types.MATERIAL
                ),
            ),
        )
        .values(
            "pk",
            "name",
            "works_amount",
            "materials_amount"
        )
    )

    return query
