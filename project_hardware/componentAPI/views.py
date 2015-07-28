from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth.models import User
from django.http import Http404

from componentAPI.serializers import ComponentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from componentAPI.models import Component
from rest_framework.decorators import api_view


@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        components = Component.objects.all()
        serializer = ComponentSerializer(components, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def post_element(request, pk):
    try:
        component= Component.objects.get(pk=pk)
    except Component.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        serializer = ComponentSerializer(component)
        return Response(serializer.data)
