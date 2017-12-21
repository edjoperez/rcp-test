#encoding: utf-8
from django.contrib.auth.models import User
import datetime
from rest_framework import serializers, viewsets, routers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email', 'is_staff')


class DateSerializer(serializers.Serializer):
    day = serializers.DateField(initial=datetime.date.today)