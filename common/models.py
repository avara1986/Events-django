# encoding: utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField(verbose_name=_("Pais"), max_length=1000, null=False, blank=False)

    def num_events(self):
        #TODO: calcular nº eventos
        pass

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Pais')
        verbose_name_plural = _('Paises')
        ordering = ('name', )


@python_2_unicode_compatible
class State(models.Model):
    name = models.CharField(verbose_name=_("Provincia"), max_length=1000, null=False, blank=False)
    country = models.ForeignKey(Country, verbose_name=_("Pais"))

    def num_events(self):
        #TODO: calcular nº eventos
        pass

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Provincia')
        verbose_name_plural = _('Provincias')
        ordering = ('name', )


@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField(verbose_name=_("Ciudad"), max_length=1000, null=False, blank=False)
    state = models.ForeignKey(State, verbose_name=_("Estado/provincia"))

    def country(self):
        return State.objects.get(id=self.state_id).country

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Ciudad')
        verbose_name_plural = _('Ciudades')
        ordering = ('name', )
