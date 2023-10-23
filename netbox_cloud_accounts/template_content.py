from extras.plugins import PluginTemplateExtension
from .models import CloudAccount

class SiteGroupCloudAccount(PluginTemplateExtension):
    model = 'dcim.sitegroup'
    
    def right_page(self):
        obj = self.context['object']
        return self.render('inc/cloud_account.html', extra_context={
            'cloud_account': CloudAccount.objects.filter(sitegroup=obj).first(),
        })
class SiteCloudAccount(PluginTemplateExtension):
    model = 'dcim.site'
    
    def right_page(self):
        obj = self.context['object']
        return self.render('inc/cloud_account.html', extra_context={
            'cloud_account': CloudAccount.objects.filter(sitegroup=obj.group).first(),
        })
template_extensions = [SiteGroupCloudAccount,SiteCloudAccount]