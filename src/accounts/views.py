from rest_framework import viewsets

from . import serializers
from . import models

class RealtorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Account.objects.filter(is_realtor=True).order_by('-registered_date')
    serializer_class = serializers.RealtorSerializer

class RealtorRatingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.RealtorRating.objects.order_by('-posted_date')
    serializer_class = serializers.RealtorRatingSerializer