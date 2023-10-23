from netbox.views import generic
from . import forms, models, tables
from utilities.views import ViewTab, register_model_view
from dcim.models import SiteGroup

class CloudAccountView(generic.ObjectView):
    queryset = models.CloudAccount.objects.all()

class CloudAccountListView(generic.ObjectListView):
    queryset = models.CloudAccount.objects.all()
    table = tables.CloudAccountTable

class CloudAccountEditView(generic.ObjectEditView):
    queryset = models.CloudAccount.objects.all()
    form = forms.CloudAccountForm

class CloudAccountDeleteView(generic.ObjectDeleteView):
    queryset = models.CloudAccount.objects.all()


#Providers
class CloudProviderView(generic.ObjectView):
    queryset = models.CloudProvider.objects.all()

class CloudProviderListView(generic.ObjectListView):
    queryset = models.CloudProvider.objects.all()
    table = tables.CloudProviderTable

class CloudProviderEditView(generic.ObjectEditView):
    queryset = models.CloudProvider.objects.all()
    form = forms.CloudProviderForm

class CloudProviderDeleteView(generic.ObjectDeleteView):
    queryset = models.CloudProvider.objects.all()


# @register_model_view(SiteGroup, name='CloudAccountsView', path='cloud-accounts')
# class CloudAccountSites(generic.ObjectView):
#     queryset = models.CloudAccounts.objects.all()
#     tab = ViewTab(
#         label='Cloud Accounts',
#     )