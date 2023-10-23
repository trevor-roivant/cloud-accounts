from extras.plugins import PluginConfig

class NetBoxCloudAccountsConfig(PluginConfig):
    name = 'netbox_cloud_accounts'
    verbose_name = 'NetBox Cloud Accounts'
    description = 'Keep inventory of cloud accounts'
    version = '0.2'
    base_url = 'cloud-accounts'
config = NetBoxCloudAccountsConfig
