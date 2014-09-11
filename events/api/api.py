#encoding: utf-8
from rest_framework import generics, permissions
from rest_framework import status
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import EventSerializer, AttendeeSerializer
from .models import Attendee, Event
#from .permissions import PostAuthorCanEditPermission


class EventList(generics.ListAPIView):
    model = Event
    serializer_class = EventSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EventDetail(generics.RetrieveAPIView):
    model = Event
    serializer_class = EventSerializer
    lookup_field = 'pk'

class AttendeeList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        attendee = Attendee.objects.all()
        serializer = AttendeeSerializer(attendee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AttendeeSerializer(data=request.DATA)
        if serializer.is_valid():
            #request.META['HTTP_ORIGIN']
            #import ipdb; ipdb.set_trace()
            event = Event.objects.get(pk=serializer.init_data['event'])
            # Puesto +2 para tests, TODO: cambiar a +1
            if event.is_open and (event.num_registereds()+2 <= event.n_seats):
                serializer.save()
                serializer.data.update({'result': True})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                serializer.data.update({'result': False})
                serializer.data.update({'error_msg': 'No quedan plazas'})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)