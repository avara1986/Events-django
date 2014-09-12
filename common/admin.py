# encoding: utf-8
from django.contrib import admin
from common.models import City, State, Country


class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ('name', 'state', 'country')


class StateAdmin(admin.ModelAdmin):
    model = State
    list_display = ('name', 'country')


class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ('name',)


admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Country, CountryAdmin)
