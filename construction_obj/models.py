from django.db import models


class Building(models.Model):
    """
    Модель объекта строительства.
    """
    name = models.CharField(max_length=50, verbose_name='наименование объекта')

    class Meta:
        verbose_name = 'объект строительства'
        verbose_name_plural = 'объекты строительства'

    def __str__(self):
        return self.name
