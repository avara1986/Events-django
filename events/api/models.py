#encoding: utf-8
import StringIO
import qrcode

from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.mail import send_mail
from django.db import models
from common.models import City, State, Country
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
#from dynamic_form.admin import *


class EventManager(models.Manager):
    def get_queryset(self):
        return super(EventManager, self).get_query_set().exclude(deleted=True)


class AttendeeManager(models.Manager):
    def get_queryset(self):
        return super(AttendeeManager, self).get_query_set().exclude(deleted=True)


class Event(models.Model):
    events = EventManager()
    objects = models.Manager()

    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=100)
    url_private = models.SlugField(verbose_name="Url interna del evento", max_length=200, null=True, blank=True)
    url_public = models.URLField(verbose_name="Url pública del evento", max_length=200, null=True, blank=True)
    n_seats = models.PositiveIntegerField(verbose_name="Número de plazas")
    n_seats_overflow = models.IntegerField()
    address = models.CharField(max_length=200)
    country = models.ForeignKey(Country, verbose_name=_("Pais"), null=True)
    state = models.ForeignKey(State, verbose_name=_("Provincia"), null=True)
    city = models.ForeignKey(City, verbose_name=_("Ciudad"), null=True)
    google_maps_url = models.CharField(max_length=200)
    google_maps_coords = models.CharField(max_length=200)
    whitelist = models.BooleanField(verbose_name="Usar whitelist", max_length=1, default=False)
    date_event = models.DateTimeField(verbose_name="Fecha de inicio")
    date_event_end = models.DateTimeField(verbose_name="Fecha de finalización")
    header = models.TextField(verbose_name="Cabecera", null=True, blank=True)
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    footer = models.TextField(verbose_name="Footer", null=True, blank=True)
    logo = models.ImageField(verbose_name="Logo", 
                                upload_to="logos",
                                null=True, blank=True)
    status = models.BooleanField(verbose_name="Activo", max_length=1, default=True)
    deleted = models.BooleanField(verbose_name="Borrado", max_length=1, default=False)

    def num_registereds(self):
        return int(Attendee.objects.filter(event=self.pk).count())

    def whitelist(self):
        return int(Whitelist.objects.filter(event=self.pk).count())

    def is_open(self):
        return bool((self.n_seats >= self.num_registereds()) and
                    (self.date_event > timezone.now()))

    def __unicode__(self):
        return "%s" % (self.title)


class Whitelist(models.Model):
    email = models.EmailField(verbose_name="Email", max_length=100)
    event = models.ManyToManyField(Event, verbose_name="Eventos", blank=True)

    def __unicode__(self):
        return "%s" % (self.email)


class Attendee(models.Model):
    objects = models.Manager()
    attendees = AttendeeManager()
    registered = models.DateTimeField(verbose_name="Fecha de registro", auto_now_add=True)
    name = models.CharField(verbose_name="Nombre", max_length=100)
    surname = models.CharField(verbose_name="Apellidos", max_length=100)
    phone = models.CharField(verbose_name="Teléfono", max_length=16, null=True, blank=True)
    email = models.EmailField(verbose_name="Email", max_length=100)
    company = models.CharField(verbose_name="Empresa", max_length=100, null=True, blank=True)
    job_title = models.CharField(verbose_name="Cargo", max_length=100, null=True, blank=True)
    web = models.URLField(verbose_name="Web", max_length=250, null=True, blank=True)
    reg_code = models.CharField(verbose_name="Localizador", max_length=100, null=True, blank=True)
    mcc = models.CharField(max_length=15, null=True, blank=True)
    id_googlepartners = models.CharField(max_length=200, null=True, blank=True)
    qr_code = models.ImageField(verbose_name="Código QR", 
                                upload_to="qrs",
                                null=True, blank=True)
    pdf_file = models.FileField(verbose_name="Fichero PDF", upload_to="pdf", null=True, blank=True)
    attended = models.BooleanField(verbose_name="Ha asistido", max_length=1, default=False)
    status = models.BooleanField(verbose_name="Activo", max_length=1, default=True)
    deleted = models.BooleanField(verbose_name="Borrado", max_length=1, default=False)
    event = models.ForeignKey(Event)

    def email_register(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def __unicode__(self):
        return "%s %s" % (self.name, self.event.title,)


def qrcode_pre_save(sender, instance, **kwargs):
    if not instance.pk:
        instance._QRCODE = True
    else:
        if hasattr(instance, '_QRCODE'):
            instance._QRCODE = False
        else:
            instance._QRCODE = True

models.signals.pre_save.connect(qrcode_pre_save, sender=Attendee)


def qrcode_post_save(sender, instance, **kwargs):

    if instance._QRCODE:
        instance._QRCODE = False
        if instance.qr_code:
            instance.qr_code.delete()
        qrCode = qrcode.QRCode(
                               version=1,
                               error_correction=qrcode.constants.ERROR_CORRECT_L,
                               box_size=10,
                               border=4,
                               )
        qrCode.add_data(instance.id)
        qrCode.make(fit=True)
        qrImage = qrCode.make_image()

        image_buffer = StringIO.StringIO()
        qrImage.save(image_buffer, 'PNG')
        image_buffer.seek(0)

        #Here we use django file storage system to save the image.
        file_name = 'QR_%s.png' % instance.id
        file_object = File(image_buffer, file_name)
        content_file = ContentFile(file_object.read())

        instance.qr_code.save(file_name, content_file, save=True)

models.signals.post_save.connect(qrcode_post_save, sender=Attendee)
