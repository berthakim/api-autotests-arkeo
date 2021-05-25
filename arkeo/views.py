from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Test
from .serializers import TestSerializer
import config


@api_view(['GET', 'POST'])
def test_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Test.objects.all()
        serializer = TestSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def test_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Test.objects.get(pk=pk)
    except Test.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TestSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TestSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
