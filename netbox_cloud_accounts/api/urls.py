from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_cloud_accounts'

router = NetBoxRouter()
router.register('cloud-account', views.CloudAccountViewSet)
router.register('cloud-provider', views.CloudProviderViewSet)
urlpatterns = router.urls