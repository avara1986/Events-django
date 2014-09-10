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

'''
class AttendeeList(generics.ListAPIView):
    model = Attendee
    serializer_class = AttendeeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = super(AttendeeList, self).get_queryset()
        return queryset.filter(event=self.kwargs.get('event'))
'''


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
            #import ipdb; ipdb.set_trace()
            event = Event.objects.get(pk=serializer.init_data['event'])
            if event.is_open and (event.num_registereds()+2 <= event.n_seats):
                serializer.save()
                serializer.data.update({'result': True})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                serializer.data.update({'result': False})
                serializer.data.update({'error_msg': 'No quedan plazas'})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
@api_view(['GET', 'PUT', 'DELETE'])
def AttendeeList(request):
    if request.method == 'GET':
        attendee = Attendee.objects.all()
        serializer = AttendeeSerializer(attendee, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AttendeeSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
