from django.contrib import admin
from construction_obj.models import (
    Building,
    Section,
    Expenditure
)


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    """
    Регистрация модели объектов строительства в админ-панели.
    """
    pass


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    """
    Регистрация модели секций сметы в админ-панели.
    """
    pass


@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    """
    Регистрация модели стоимости секций сметы в админ-панели.
    """
    list_display = 'section', 'name', 'type', 'count', 'price',
