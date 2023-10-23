from netbox.forms import NetBoxModelForm
from .models import CloudAccount, CloudProvider
from django import forms
from tenancy.models import ContactGroup, Contact, Tenant
from utilities.forms.fields import (
    DynamicModelChoiceField, CSVModelChoiceField,
    DynamicModelMultipleChoiceField,
    TagFilterField, CSVChoiceField,
)

class CloudAccountForm(NetBoxModelForm):
    accountId = forms.CharField(
        required=True,
        label='ID'
    )
    contactgroup = DynamicModelChoiceField(
        queryset=ContactGroup.objects.all(),
        label='Contact Group',
        required=False
    )
    contact = DynamicModelChoiceField(
        queryset=Contact.objects.all(),
        label='Contact',
        required=False
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        label='Tenant',
        required=False
    )
    provider = DynamicModelChoiceField(
        queryset=CloudProvider.objects.all(),
        label='Provider',
        required=False
    )
    class Meta:
        model = CloudAccount
        fields = ('name', 'accountId', 'status' , 'provider', 'tenant', 'contact','contactgroup','sitegroup')

class CloudProviderForm(NetBoxModelForm):
    contactgroup = DynamicModelChoiceField(
        queryset=ContactGroup.objects.all(),
        label='Contact Group',
        required=False
    )

    class Meta:
        model = CloudProvider
        fields = ('name', 'contactgroup')