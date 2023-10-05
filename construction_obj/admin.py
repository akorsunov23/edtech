from django.contrib import admin
from construction_obj.models import Building


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    """
    Регистрация модели объектов строительства в админ-панели.
    """
    pass
