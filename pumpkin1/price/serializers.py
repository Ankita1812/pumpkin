from rest_framework import serializers

from django.contrib.auth.models import User
from price.models import Pumpkin


# Serializers define the API representation.
class PumpkinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pumpkin
        fields = '__all__'

