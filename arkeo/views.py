# from .models import MeteoStation
# from .serializers import MeteoStationSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

from arkeo.models import MeteoStation
from django.contrib.auth.models import User
from arkeo.serializers import MeteoStationSerializer, UserSerializer
from arkeo.permissions import IsOwnerOrReadOnly
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics


class MeteoStationList(APIView):
    """
    List all MeteoStations, or create a new Meteo Station.
    """

    def get(self, request, format=None):
        stations = MeteoStation.objects.all()
        serializer = MeteoStationSerializer(stations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MeteoStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # associating stations with Users
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MeteoStationDetail(APIView):
    """
    Retrieve, update or delete a station instance.
    """

    def get_object(self, pk):
        try:
            return MeteoStation.objects.get(pk=pk)
        except MeteoStation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        station = self.get_object(pk)
        serializer = MeteoStationSerializer(station)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        station = self.get_object(pk)
        serializer = MeteoStationSerializer(station, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        station = self.get_object(pk)
        station.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
