from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from apps.common.mixins import TimeStampedModel

# Create your models here.


class JobScraped(TimeStampedModel):

    title = models.CharField(max_length=5000, null=True, blank=True)
    company  = models.CharField(max_length=5000, null=True, blank=True)
    announcement = models.CharField(max_length=5000, null=True, blank=True)
    description = models.CharField(max_length=500000, null=True, blank=True)
