from django.db import models
from django.db.models import Sum, F

from construction_obj.models import Section, Building, Expenditure
from decimal import Decimal


def get_parent_sections(building_id: int) -> list[Section]:
    """
    Получение данных о родительских секциях объекта.
    :param building_id: ID объекта.
    :return Полученные данные из БД, с суммарной стоимостью по родительским секциям.
    """
    query = (
        Section.objects
        .filter(parent__building_id=building_id)
        .values(
            "parent_id",
            "parent__name"
        )
        .annotate(
            total_price=Sum(
                F("expenditure__price")
                * F("expenditure__count")
                )
        )
    )

    return query


def get_buildings() -> list[dict]:
    """
    Получение списка объектов со стоимостью по типу.
    :return Полученные данные из БД, с суммарной стоимостью по типам.
    """
    query = (
        Building.objects.all()
        .annotate(
            works_amount=Sum(
                F("section__expenditure__price")
                * F("section__expenditure__count"),
                filter=models.Q(
                    section__expenditure__type=Expenditure.Types.WORK
                ),
            ),
            materials_amount=Sum(
                F("section__expenditure__price")
                * F("section__expenditure__count"),
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


def update_with_discount(section_id: int, discount: Decimal):
    """
    Применение скидки к вложенным секциям.
    :param section_id: ID родительской секции.
    :param discount: Размер скидки.
    :return None.
    """
    (
        Expenditure.objects
        .filter(section__parent_id=section_id)
        .update(
            price=F("price") * (1 - discount / 100)
        )
    )
