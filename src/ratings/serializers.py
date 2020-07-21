from rest_framework import serializers

from . import models

class ListingRatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ListingRating
        fields = '__all__'
