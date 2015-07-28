from django.contrib.auth.models import User

from rest_framework import serializers
from models import Component
class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id', 'compId', 'compName')
