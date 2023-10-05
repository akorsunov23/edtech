from decimal import Decimal

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from construction_obj.forms import DiscountForms
from construction_obj.services import (
    get_parent_sections,
    get_buildings,
    update_with_discount
)


class ListBuildingView(ListView):
    """
    Список всех объектов с подсчитанными
    затратами на строительство.
    """

    template_name = "construction_obj/list_building.html"
    context_object_name = "buildings"

    def get_queryset(self):
        query = get_buildings()
        return query


class DetailBuildingView(ListView):
    """
    Детальная информация об объекте с секциями и общей стоимостью затрат.
    """

    template_name = "construction_obj/detail_building.html"
    context_object_name = "sections"

    def get_queryset(self):
        obj_id = self.kwargs["pk"]
        query = get_parent_sections(building_id=obj_id)
        return query


class UpdateSectionView(FormView):
    """
    Применение скидки к стоимости секции.
    """
    template_name = "construction_obj/update_section.html"
    success_url = reverse_lazy("construction_obj:list_buildings")
    form_class = DiscountForms

    def form_valid(self, form):
        """
        Применяем скидку ко вложенным секциям.
        """
        section_id = self.kwargs['pk']
        discount = Decimal(self.request.POST.get('discount'))
        update_with_discount(
            section_id=section_id,
            discount=discount
        )
        return HttpResponseRedirect(self.success_url)
