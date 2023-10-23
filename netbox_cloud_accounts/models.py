from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from .choices import AccountStatusChoices
from django.urls import reverse

class CloudAccount(NetBoxModel):
    name = models.CharField(
        max_length=32
    )

    display = models.CharField(
        max_length=32,
        blank=True,
        null=True
        )

    accountId = models.CharField(
        help_text='Account Identifier',
        max_length=32,
        unique = True
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=50,
        choices=AccountStatusChoices,
        default=AccountStatusChoices.STATUS_ACTIVE
    )
    contact = models.ForeignKey(
        help_text='Account Owner',
        to='tenancy.Contact',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True,
    )
    contactgroup = models.ForeignKey(
        help_text='Account Owner',
        to='tenancy.contactgroup',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True,
    )
    sitegroup = models.ForeignKey(
        help_text='Site Group',
        to='dcim.sitegroup',
        on_delete=models.PROTECT,
        related_name="+",
        blank=True,
        null=True
    )
    provider = models.ForeignKey(
        help_text='Cloud Provider',
        to='CloudProvider',
        on_delete=models.PROTECT,
        related_name="+",
        blank=True,
        null=True
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )
    comments = models.TextField(
        blank=True
    )
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_cloud_accounts:cloudaccount', args=[self.pk])
    def get_status_color(self):
        return AccountStatusChoices.colors.get(self.status)
class CloudProvider(NetBoxModel):
    name = models.CharField(
        max_length=32
    )
    display = models.CharField(
        max_length=32,
        blank=True,
        null=True
        )
    contactgroup = models.ForeignKey(
        help_text='Account Group',
        to='tenancy.contactgroup',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True,
    )
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_cloud_accounts:cloudprovider', args=[self.pk])