from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Test
from .serializers import TestSerializer


class TestList(APIView):

    def get(self, request):
        test1 = Test.objects.all()
        serializer = TestSerializer(test1, many=True)
        return Response(serializer.data)


    def post(self):
        pass


    def put(self):
    	pass


    def delete(self):
    	pass


    def path(self):
    	pass


    def head(self):
    	pass


    def options(self):
    	pass

# def arkeo_api(request):
#     return render(request, 'arkeo/arkeo_api.html', {'title': 'About'})
