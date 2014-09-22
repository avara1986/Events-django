# encoding: utf-8
from functools import partial
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from events.api.models import Event, Attendee, Whitelist
from events.api.forms import EventsChangeForm
from dynamic_form.admin import QuestionInline, AnswerInline


class WhitelistAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['email', ]
    list_display = ('email', )
    filter_horizontal = ("event", )

    class Meta:
        app_label = "Event"

    class Media:
        css = {
            'all': ('/static/admin/css/admin.css',)
            }


class AttendeeAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['name', 'surname', 'email']
    list_display = ('registered', 'event', 'name', 'surname', 'email')

    inlines = [
               AnswerInline
               ]

    def get_export_queryset(self, request):
        """
        Returns export queryset.

        Default implementation respects applied search and filters.
        """
        # copied from django/contrib/admin/options.py
        list_display = self.get_list_display(request)
        list_display_links = self.get_list_display_links(request, list_display)

        ChangeList = self.get_changelist(request)
        cl = ChangeList(request, self.model, list_display,
                        list_display_links, self.list_filter,
                        self.date_hierarchy, self.search_fields,
                        self.list_select_related, self.list_per_page,
                        self.list_max_show_all, self.list_editable,
                        self)

        # query_set has been renamed to queryset in Django 1.8
        try:
            return cl.queryset
        except AttributeError:
            # If super-user, show all comments
            #import ipdb; ipdb.set_trace()
            if request.user.is_superuser:
                return cl.query_set
            if request.user.groups.all().count() > 0:
                return cl.query_set.filter(event__group__in=(request.user.groups.all()))

            return cl.query_set.filter(event__created_by=request.user)
            return cl.query_set

    def queryset(self, request):
        qs = super(AttendeeAdmin, self).queryset(request)
        # If super-user, show all comments
        if request.user.is_superuser:
            return qs
        #import ipdb; ipdb.set_trace()
        if request.user.groups.all().count() > 0:
            return qs.filter(event__group__in=(request.user.groups.all()))

        return qs.filter(event__created_by=request.user)

    class Media:
        css = {
            'all': ('/static/admin/css/admin.css',)
            }


class EventAdmin(admin.ModelAdmin):
    form = EventsChangeForm
    search_fields = ['name', 'title', 'address']
    list_display = ('title', 'n_seats', 'address', 'num_registereds', 'is_open', 'date_event', 'date_event_end','num_whitelisted')
    readonly_fields = ('created_by', )

    inlines = [
               QuestionInline
               ]

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['created_by', 'group']
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
        #import ipdb; ipdb.set_trace()
        if request.user.groups.all().count() > 0:
            return qs.filter(group=(request.user.groups.all()))

        return qs.filter(created_by=request.user)

    def get_form(self, request, obj=None, **kwargs):
        kwargs['formfield_callback'] = partial(self.formfield_for_dbfield, request=request)
        return super(EventAdmin, self).get_form(request, obj, **kwargs)

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(EventAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'group':
            field.queryset = field.queryset.filter(id__in=(kwargs['request'].user.groups.all()))
        return field

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
