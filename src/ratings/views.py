from rest_framework import viewsets
# from rest_framework import generics

from . import serializers
from . import models

# class ListingList(generics.ListCreateAPIView):
class ListingRatingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.ListingRating.objects.all()
    serializer_class = serializers.ListingRatingSerializer
