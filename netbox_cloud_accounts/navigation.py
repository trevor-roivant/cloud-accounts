from extras.plugins import PluginMenu , PluginMenuItem, PluginMenuButton
from utilities.choices import ButtonColorChoices

ca_menu_items =   ( 
    PluginMenuItem(
        link='plugins:netbox_cloud_accounts:cloudaccount_list',
        link_text='Accounts',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_cloud_accounts:cloudaccount_add',
                title='Accounts',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,

            ),
        ),
    ),
    )
p_menu_items =   ( 
    PluginMenuItem(
        link='plugins:netbox_cloud_accounts:cloudprovider_list',
        link_text='Providers',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_cloud_accounts:cloudprovider_add',
                title='Providers',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,

            ),
        ),
    ),
    )
menu = PluginMenu(
    label='Cloud Environments',
    groups=(
        ('Cloud Accounts', ca_menu_items),
        ('Providers', p_menu_items),
    ),
    icon_class='mdi mdi-cloud-outline'
)