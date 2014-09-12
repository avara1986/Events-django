from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from events.api.models import Event, Attendee

from events.api.forms import EventsChangeForm

class AttendeeAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['name', 'surname', 'email', 'company']
    list_display = ('registered', 'name', 'surname', 'email', 'company')


class EventAdmin(admin.ModelAdmin):
    form = EventsChangeForm
    search_fields = ['name', 'title', 'address']
    list_display = ('title', 'url', 'n_seats', 'address', 'num_registereds', 'is_open', 'date_event')

    class Media:
            js = ('http://ajax.googleapis.com/ajax/libs/jquery/1.4.0/jquery.min.js',
                    '/static/admin/js/states.js')

admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)
