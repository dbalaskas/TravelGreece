from rest_framework import viewsets

from . import serializers
from . import models

class ContractViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Contract.objects.order_by('-deal_date')
    serializer_class = serializers.ContractSerializer