#encoding: utf-8
import re
from rest_framework import generics, permissions
from rest_framework import status
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from common.serializers import CitySerializer, StateSerializer, CountrySerializer
from common.models import City, State, Country


class CityList(generics.ListAPIView):
    model = City
    serializer_class = CitySerializer
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = 'state'

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        state = self.kwargs['state']
        return City.objects.filter(state=state)

class StateList(generics.ListAPIView):
    model = State
    serializer_class = StateSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = 'country'

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        country = self.kwargs['country']
        return State.objects.filter(country=country)


class CountryList(generics.ListAPIView):
    model = Country
    serializer_class = CountrySerializer
    permission_classes = [
        permissions.AllowAny
    ]
