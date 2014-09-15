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
    save_as = True

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.created_by = request.user
            #obj.last_modified_by = request.user
            obj.save()

    def queryset(self, request):
        qs = super(EventAdmin, self).queryset(request)
        # If super-user, show all comments
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user)

    class Media:
            js = ('/static/jquery/jquery.min.js',
                    '/static/admin/js/event_states.js',
                    '/static/admin/js/event_cities.js',
                    '/static/admin/js/ckeditor/ckeditor.js',
                    '/static/admin/js/event_ckeditor.js',)

admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)
