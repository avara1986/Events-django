from rest_framework import serializers

from common.models import City, State, Country #User, Post, Photo


class CitySerializer(serializers.ModelSerializer):
    country = serializers.Field()

    class Meta:
        model = City
        fields = ('id', 'name', 'state', 'country',)

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'name', 'country',)


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name',)

