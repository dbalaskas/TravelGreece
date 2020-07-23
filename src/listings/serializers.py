from rest_framework import serializers

from . import models

class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Listing
        fields = '__all__'

class ListingRatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ListingRating
        fields = '__all__'