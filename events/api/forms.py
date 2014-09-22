# encoding: utf-8
from django import forms
from django.contrib.auth.models import Group
from django.forms import widgets
from django.forms.util import flatatt
from django.utils.encoding import smart_unicode
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from events.api.models import Event
from common.models import Country, State, City


class StateChoiceWidget(widgets.Select):
    def render(self, name, value, attrs=None, choices=()):
        self.choices = [(u"", u"---------")]
        if value is None:
            value = ''
        else:
            obj = State.objects.get(id=value)
            for m in State.objects.filter(country=obj.country):
                self.choices.append((m.id, smart_unicode(m)))
        final_attrs = self.build_attrs(attrs, name=name)
        output = [u'<select%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append('</select>')
        return mark_safe(u'\n'.join(output))


class CityChoiceWidget(widgets.Select):
    def render(self, name, value, attrs=None, choices=()):
        self.choices = [(u"", u"---------")]
        if value is None:
            value = ''
        else:
            obj = City.objects.get(id=value)
            for m in City.objects.filter(state=obj.state):
                self.choices.append((m.id, smart_unicode(m)))
        final_attrs = self.build_attrs(attrs, name=name)
        output = [u'<select%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append('</select>')
        return mark_safe(u'\n'.join(output))


class EventsChangeForm(forms.ModelForm):
    #group = forms.ModelChoiceField(Group.objects.filter(),
    #            label=ugettext_lazy("Grupos"), required=False)
    state = forms.ModelChoiceField(State.objects,
                widget=StateChoiceWidget(),
                label=ugettext_lazy("Provincia"), required=False)

    city = forms.ModelChoiceField(City.objects,
                widget=CityChoiceWidget(),
                label=ugettext_lazy("Ciudad"), required=False)

    class Meta:
        model = Event

    def __init__(self, *args, **kwargs):
        super(EventsChangeForm, self).__init__(*args, **kwargs)
