from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import CloudAccount, CloudProvider


class NestedCloudAccountSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_cloud_accounts-api:cloudaccount-detail'
    )

    class Meta:
        model = CloudAccount
        fields = ('id', 'url', 'display', 'name')


class CloudAccountSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_cloud_accounts-api:cloudaccount-detail'
    )
    class Meta:
        model = CloudAccount
        fields = (
            'id', 'url', 'name', 'display', 'tenant','provider', 'comments', 'contact','contactgroup', 'sitegroup', 'accountId','status', 'tags', 'created',
            'last_updated',
        )
        sitegroup = NestedCloudAccountSerializer()


class NestedCloudProviderSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_cloud_accounts-api:cloudprovider-detail'
    )

    class Meta:
        model = CloudAccount
        fields = ('id', 'url', 'display', 'name')



class CloudProviderSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_cloud_accounts-api:cloudprovider-detail'
    )
    class Meta:
        model = CloudProvider
        fields = (
            'id', 'url', 'name', 'contactgroup', 'tags', 'created',
            'last_updated',
        )
        