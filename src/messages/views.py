from rest_framework import viewsets

from . import serializers
from . import models

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Message.objects.order_by('-date')
    serializer_class = serializers.MessageSerializer
