from django.contrib import admin
from construction_est.models import Section, Expenditure


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
    pass
