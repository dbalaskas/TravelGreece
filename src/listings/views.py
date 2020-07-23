from rest_framework import viewsets

from . import serializers
from . import models

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Listing.objects.filter(is_published=True).order_by('-list_date')
    serializer_class = serializers.ListingSerializer

class ListingRatingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.ListingRating.objects.filter(listing__is_published=True).order_by('-posted_date')
    serializer_class = serializers.ListingRatingSerializer

