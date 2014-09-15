#encoding: utf-8
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from common.models import City, State, Country
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


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
    url = models.CharField(verbose_name="Url del evento", max_length=200, null=True, blank=True)
    n_seats = models.PositiveIntegerField(verbose_name="Número de plazas")
    n_seats_overflow = models.IntegerField()
    address = models.CharField(max_length=200)
    country = models.ForeignKey(Country, verbose_name=_("Pais"), null=True)
    state = models.ForeignKey(State, verbose_name=_("Provincia"), null=True)
    city = models.ForeignKey(City, verbose_name=_("Ciudad"), null=True)
    google_maps_url = models.CharField(max_length=200)
    google_maps_coords = models.CharField(max_length=200)
    date_event = models.DateTimeField(verbose_name="Fecha de inicio")
    date_event_end = models.DateTimeField(verbose_name="Fecha de finalización")
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    status = models.BooleanField(verbose_name="Activo", max_length=1, default=True)
    deleted = models.BooleanField(verbose_name="Borrado", max_length=1, default=False)

    def num_registereds(self):
        return int(Attendee.objects.filter(event=self.pk).count())

    def is_open(self):
        return bool((self.n_seats >= self.num_registereds()) and
                    (self.date_event > timezone.now()))

    def __unicode__(self):
        return "%s %s %s" % (self.title, self.url, self.n_seats)

    def __str__(self):
        return "%s %s %s" % (self.title, self.url, self.n_seats)


class Attendee(models.Model):
    objects = models.Manager()
    attendees = AttendeeManager()

    registered = models.DateTimeField(verbose_name="Fecha de registro", auto_now_add=True)
    name = models.CharField(verbose_name="Nombre", max_length=100)
    surname = models.CharField(verbose_name="Apellidos", max_length=100)
    phone = models.CharField(verbose_name="Teléfono", max_length=16, null=True, blank=True)
    email = models.CharField(verbose_name="Email", max_length=100)
    company = models.CharField(verbose_name="Empresa", max_length=100, null=True, blank=True)
    job_title = models.CharField(verbose_name="Cargo", max_length=100, null=True, blank=True)
    web = models.CharField(verbose_name="Web", max_length=250, null=True, blank=True)
    reg_code = models.CharField(verbose_name="Localizador", max_length=100, null=True, blank=True)
    qr_code = models.ImageField(verbose_name="Código QR", 
                                upload_to="media/landing/qr/",
                                height_field="300",
                                width_field="300", null=True, blank=True)
    pdf_file = models.FileField(verbose_name="Fichero PDF", upload_to="media/landing/pdf/", null=True, blank=True)
    attended = models.BooleanField(verbose_name="Ha asistido", max_length=1, default=False)
    status = models.BooleanField(verbose_name="Activo", max_length=1, default=True)
    deleted = models.BooleanField(verbose_name="Borrado", max_length=1, default=False)
    event = models.ForeignKey(Event)

    def email_reguster(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def __unicode__(self):
        return "%s %s" % (self.name, self.event.title,)
