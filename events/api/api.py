#encoding: utf-8
import re
from rest_framework import generics, permissions
from rest_framework import status
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from events.api.serializers import EventSerializer, AttendeeSerializer
from events.api.models import Attendee, Event
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
    def get(self, request):
        attendee = Attendee.objects.all()
        serializer = AttendeeSerializer(attendee, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AttendeeSerializer(data=request.DATA)
        serializer.data.update({'result': False})
        if serializer.is_valid():

            #import ipdb; ipdb.set_trace()
            event = Event.objects.get(pk=serializer.init_data['event'])
            '''
            Si la URL pública se ha definido, se verifica que solo pueden venir registros desde esa URL
            '''
            if event.url_public != "" and event.url_public is not None:
                #import ipdb; ipdb.set_trace()
                if 'HTTP_ORIGIN' in  request.META.keys():
                    requestURL = request.META['HTTP_ORIGIN']
                else:
                    requestURL = request.META['HTTP_REFERER']

                if not re.search(event.url_public, requestURL):
                    serializer.data.update({'error_msg': 'No está permitido registrarse desde %s' % requestURL })
                    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            '''
            Se verifica el número de plazas
            '''
            if event.is_open and ((event.num_registereds() + 1) <= event.n_seats):
                #serializer.object.qr_code=""
                serializer.save()
                serializer.data.update({'result': True})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:

                serializer.data.update({'error_msg': 'No quedan plazas'})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
