from django.db import models
from django.utils.translation import ugettext as _


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Date updated'))

    class Meta:
        abstract = True


class Seller(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Seller name')
    )
    birthday = models.DateField(
        verbose_name=_('Seller birthday')
    )

    class Meta:
        verbose_name = _('Seller')
        verbose_name_plural = _('Sellers')


class Product(TimeStampedModel):
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_('Product name'),
        null=True, blank=True
    )
    description = models.TextField(
        verbose_name=_('Product description'),
        null=True, blank=True
    )

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

