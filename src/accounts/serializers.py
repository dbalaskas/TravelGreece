from rest_framework import serializers

from . import models

class RealtorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'

class RealtorRatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RealtorRating
        fields = '__all__'