from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers import CloudAccountSerializer, CloudProviderSerializer


class CloudAccountViewSet(NetBoxModelViewSet):
    queryset = models.CloudAccount.objects.prefetch_related('tags')
    serializer_class = CloudAccountSerializer

class CloudProviderViewSet(NetBoxModelViewSet):
    queryset = models.CloudProvider.objects.prefetch_related('tags')
    serializer_class = CloudProviderSerializer