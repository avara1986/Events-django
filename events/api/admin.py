from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from .models import Event, Attendee


class AttendeeAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['name', 'surname', 'email', 'company']
    list_display = ('registered', 'name', 'surname', 'email', 'company')


class EventAdmin(admin.ModelAdmin):
    search_fields = ['name', 'title', 'address']
    list_display = ('title', 'url', 'n_seats', 'address', 'num_registereds', 'date_event')

admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)
