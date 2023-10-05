from django.db import models
from django.db.models import Sum, F
from django.views.generic import ListView, DetailView
from construction_obj.models import Building, Section, Expenditure
from construction_obj.services import get_parent_sections, get_buildings


class ListBuilding(ListView):
    """
    Список всех объектов с подсчитанными
    затратами на строительство.
    """

    template_name = "construction_obj/list_building.html"
    context_object_name = "buildings"

    def get_queryset(self):
        query = get_buildings()
        return query


class DetailBuilding(ListView):
    """
    Детальная информация об объекте с секциями и общей стоимостью затрат.
    """

    template_name = "construction_obj/detail_building.html"
    context_object_name = "sections"

    def get_queryset(self):
        obj_id = self.kwargs["pk"]
        query = get_parent_sections(building_id=obj_id)
        return query
