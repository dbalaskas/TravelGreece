from rest_framework import serializers
from . import models


class ContractSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Contract
        fields = '__all__'