from rest_framework import serializers

from dynamic_form.models import Question, Answer
from .models import Attendee, Event


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'slug', 'question', 'required', 'type')


class AsnwerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer')


class EventSerializer(serializers.ModelSerializer):
    num_registereds = serializers.Field()
    is_open = serializers.Field()
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'url_public', 'n_seats', 'n_seats_overflow',
                  'address', 'city', 'google_maps_url', 'google_maps_coords',
                  'date_event', 'num_registereds', 'is_open', 'questions')


class AttendeeSerializer(serializers.ModelSerializer):
    answers = AsnwerSerializer(many=True)

    class Meta:
        model = Attendee
        fields = ('id', 'event', 'name', 'surname', 'email', 'answers')



'''
class AttendeeSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=16)
    email = serializers.CharField(max_length=100)
    company = serializers.CharField(max_length=100)
    web = serializers.CharField(max_length=250)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new Attendee instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('name', instance.name)
            instance.surname = attrs.get('surname', instance.surname)
            instance.phone = attrs.get('phone', instance.phone)
            instance.email = attrs.get('email', instance.email)
            instance.company = attrs.get('company', instance.company)
            instance.web = attrs.get('web', instance.web)
            return instance

        # Create new instance
        return Attendee(**attrs)
'''