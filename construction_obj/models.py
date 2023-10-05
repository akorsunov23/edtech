from django.db import models
from django.core.exceptions import ValidationError


class Building(models.Model):
    """
    Модель объекта строительства.
    """

    name = models.CharField(max_length=50, verbose_name="наименование объекта")

    class Meta:
        verbose_name = "объект строительства"
        verbose_name_plural = "объекты строительства"

    def __str__(self):
        return self.name


class Section(models.Model):
    """
    Модель секций сметы.
    """

    name = models.CharField(max_length=50, verbose_name="название сметы")
    building = models.ForeignKey(
        Building, on_delete=models.PROTECT, verbose_name="объект строительства"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        verbose_name="родительская секция",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "секция сметы"
        verbose_name_plural = "секции смет"

    def save(
            self,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None
    ):
        """Перед сохранением проверяем на уровень вложенности."""
        if not self.id and self.parent and getattr(self.parent, "parent", None):
            raise ValidationError("Максимальный уровень вложенности 2")
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        if self.parent:
            return "{parent} - {name}".format(
                parent=self.parent,
                name=self.name
            )
        return "{name}: {object_name}".format(
            name=self.name,
            object_name=self.building.name
        )


class Expenditure(models.Model):
    """
    Модель стоимости сметы.
    """

    class Types:
        WORK = "work"
        MATERIAL = "material"
        choices = (
            (WORK, "Работа"),
            (MATERIAL, "Материал"),
        )

    section = models.ForeignKey(
        Section,
        on_delete=models.PROTECT,
        help_text="Расценка может принадлежать "
                  "только той секции, у которой указан parent",
    )
    name = models.CharField(max_length=50, verbose_name="название расценки")
    type = models.CharField(
        verbose_name="тип расценки", choices=Types.choices, max_length=8
    )
    count = models.DecimalField(
        verbose_name="кол-во", max_digits=20, decimal_places=8
    )
    price = models.DecimalField(
        verbose_name="цена за единицу", max_digits=20, decimal_places=2
    )

    class Meta:
        verbose_name = "расценка сметы"
        verbose_name_plural = "расценки смет"
