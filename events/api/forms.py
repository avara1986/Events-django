# encoding: utf-8
from django import forms
from django.forms import widgets
from django.forms.util import flatatt
from django.utils.encoding import smart_unicode
from django.utils.safestring import mark_safe
from django.contrib import admin
from django.utils.translation import ugettext_lazy

from events.api.models import Event
from common.models import Country, State


class StateChoiceWidget(widgets.Select):
    def render(self, name, value, attrs=None, choices=()):
        self.choices = [(u"", u"---------")]
        if value is None:
            # if no municipality has been previously selected,
            # render either an empty list or, if a country has
            # been selected, render its municipalities
            value = ''
            #import ipdb; ipdb.set_trace()
            '''
            model_obj = self.form_instance.instance
            if model_obj and model_obj.country:
                for m in model_obj.country.state_set.all():
                    self.choices.append((m.id, smart_unicode(m)))
            '''
        else:
            # if a municipality X has been selected,
            # render only these municipalities, that belong
            # to X's country
            obj = State.objects.get(id=value)
            for m in State.objects.filter(country=obj.country):
                self.choices.append((m.id, smart_unicode(m)))

        # copy-paste from widgets.Select.render
        final_attrs = self.build_attrs(attrs, name=name)
        output = [u'<select%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append('</select>')
        return mark_safe(u'\n'.join(output))


class EventsChangeForm(forms.ModelForm):
    state = forms.ModelChoiceField(State.objects,
                widget=StateChoiceWidget(),
                label=ugettext_lazy("Provincia"), required=False)

    class Meta:
        model = Event

    def __init__(self, *args, **kwargs):
        super(EventsChangeForm, self).__init__(*args, **kwargs)
