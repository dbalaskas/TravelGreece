from rest_framework import viewsets
# from rest_framework import generics

from . import serializers
from . import models

# class ListingList(generics.ListCreateAPIView):
class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Listing.objects.all()
    serializer_class = serializers.ListingSerializer

