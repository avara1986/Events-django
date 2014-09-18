# encoding: utf-8
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from events.api.models import Event, Attendee, Whitelist
from events.api.forms import EventsChangeForm


class WhitelistAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['email', ]
    list_display = ('email', )
    filter_horizontal = ("event", )

    class Meta:
        app_label = "event"

    class Media:
        css = {
            'all': ('/static/admin/css/admin.css',)
            }


class AttendeeAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['name', 'surname', 'email', 'company']
    list_display = ('registered', 'name', 'surname', 'email', 'company')

    class Meta:
        app_label = "Event"

    class Media:
        css = {
            'all': ('/static/admin/css/admin.css',)
            }


class EventAdmin(admin.ModelAdmin):
    form = EventsChangeForm
    search_fields = ['name', 'title', 'address']
    list_display = ('title', 'n_seats', 'address', 'num_registereds', 'is_open', 'date_event')
    readonly_fields = ('created_by', )

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['created_by',]
        }),
        ('Configuración', {
            'classes': ('collapse',),
            'fields': ['title', 'url_private', 'url_public', 'n_seats', 'n_seats_overflow']}),
        ('Información', {
            'classes': ('collapse',),
            'fields': ['date_event', 'date_event_end', 'country', 'state', 'city', 'address', 'google_maps_url', 'google_maps_coords', ]}),
        ('Landing', {
            'classes': ('collapse',),
            'fields': ['header', 'description', 'footer', 'logo']}),
    ]
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

    class Meta:
        app_label = "Event"

    class Media:
            js = ('/static/jquery/jquery.min.js',
                    '/static/admin/js/event_states.js',
                    '/static/admin/js/event_cities.js',
                    '/static/admin/js/ckeditor/ckeditor.js',
                    '/static/admin/js/event_ckeditor.js',)

admin.site.register(Whitelist, WhitelistAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)
