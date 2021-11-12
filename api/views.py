from django.http import HttpResponse, JsonResponse
from urlhandler import models as model
import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DataSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, day, month, year):
    """
    Retrieve, update or delete a code snippet.
    """
    try:

        snippet = model.Data.objects.all()

    except model.Data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DataSerializer(snippet, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DataSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)