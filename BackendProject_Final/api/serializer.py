# Here, we have to create serializers for our data model, so that its records can be serialized (or transformed) into something
#   the Response object can understand & return to our user

from rest_framework import serializers
from blinkapp.models import *

class blinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = blnk
        fields = '__all__'

class blinkCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = blnk
        fields = ['blink_count']#'__all__'