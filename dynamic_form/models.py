# encoding: utf-8

from django.conf import settings
#from events.settings import DYNAMIC_FORM_MODEL_IMPORT, DYNAMIC_FORM_QUESTION_FK_MODEL, DYNAMIC_FORM_ANSWER_FK_MODEL
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
#from DYNAMIC_FORM_MODEL_IMPORT import DYNAMIC_FORM_QUESTION_FK_MODEL, DYNAMIC_FORM_ANSWER_FK_MODEL
#importlib.import_module(DYNAMIC_FORM_MODEL_IMPORT)
from events.api.models import Event, Attendee, Whitelist
#myModel = DYNAMIC_FORM_MODEL_IMPORT + '.Event'
INPUT_TYPES = (
    ('text', _('Texto')),
    ('textarea', _('Caja de texto')),
    ('email', _('Email')),
    ('checkbox', _('Opciones (Checkbox)')),
    ('select', _('Opciones (Seleccionable)')),
    ('radio', _('Opciones (Radio)')),
)


@python_2_unicode_compatible
class Question(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(verbose_name="Identificador",
                               help_text="Se utilizará para crear el formulario\
                               en su landing correspondiente",
                               max_length=250, unique=True, null=False)
    question = models.CharField(verbose_name="Pregunta", max_length=250)
    required = models.BooleanField(verbose_name="Campo obligatorio", default=True)
    type = models.CharField(verbose_name=_('Tipo de campo'), max_length=15,
                                  choices=INPUT_TYPES, default='text')
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    questioner = models.ForeignKey(settings.DYNAMIC_FORM_QUESTION_MODEL, verbose_name=_('Formulario'), related_name='questions')

    def __str__(self):
        return '%s' % (self.question)


class Answer(models.Model):
    answerer = models.ForeignKey(settings.DYNAMIC_FORM_ANSWER_MODEL, verbose_name=_('Respondedor'), related_name='answers')
    question = models.ForeignKey(Question, verbose_name=_('Pregunta'))
    answer = models.TextField(verbose_name=_('Respuesta'))

    def __str__(self):
        return '%s' % (self.answer)
