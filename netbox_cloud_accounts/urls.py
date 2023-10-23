from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (
    path('cloud-accounts/', views.CloudAccountListView.as_view(), name='cloudaccount_list'),
    path('cloud-accounts/add/', views.CloudAccountEditView.as_view(), name='cloudaccount_add'),
    path('cloud-accounts/<int:pk>/', views.CloudAccountView.as_view(), name='cloudaccount'),
    path('cloud-accounts/<int:pk>/edit/', views.CloudAccountEditView.as_view(), name='cloudaccount_edit'),
    path('cloud-accounts/<int:pk>/delete/', views.CloudAccountDeleteView.as_view(), name='cloudaccount_delete'),
    path('cloud-accounts/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='cloudaccount_changelog', kwargs={
        'model': models.CloudAccount
    }),
    path('cloud-provider/', views.CloudProviderListView.as_view(), name='cloudprovider_list'),
    path('cloud-provider/add/', views.CloudProviderEditView.as_view(), name='cloudprovider_add'),
    path('cloud-provider/<int:pk>/', views.CloudProviderView.as_view(), name='cloudprovider'),
    path('cloud-provider/<int:pk>/edit/', views.CloudProviderEditView.as_view(), name='cloudprovider_edit'),
    path('cloud-provider/<int:pk>/delete/', views.CloudProviderDeleteView.as_view(), name='cloudprovider_delete'),
    path('cloud-provider/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='cloudprovider_changelog', kwargs={
        'model': models.CloudProvider
    })
    
    
)