import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import CloudAccount, CloudProvider

class CloudAccountTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()
    class Meta(NetBoxTable.Meta):
        model = CloudAccount
        fields = ('pk', 'id', 'name','provider', 'tenant', 'comments', 'accountId','status')
        default_columns = ('name', 'accountId','provider','tenant','status')

class CloudProviderTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = CloudProvider
        fields = ('pk', 'id', 'name')
        default_columns = ('name',)