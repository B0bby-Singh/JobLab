from django.db import models


class TimeStampedModel(models.Model):
    """Mixin to track model time stamp"""
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True