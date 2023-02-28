from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from apps.common.mixins import TimeStampedModel

# Create your models here.


class JobScraped(TimeStampedModel):

    title = models.CharField(max_length=5000, null=True, blank=True)
    company  = models.CharField(max_length=5000, null=True, blank=True)
    announcement = models.CharField(max_length=5000, null=True, blank=True)
    description = models.CharField(max_length=500000, null=True, blank=True)


class Job(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=-1)
    companyname = models.CharField(db_column='companyName', max_length=-1)  # Field name made lowercase.
    location = models.CharField(max_length=-1, blank=True, null=True)
    via = models.CharField(max_length=-1, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    thumbnail = models.CharField(max_length=-1, blank=True, null=True)
    applylink = models.CharField(db_column='applyLink', unique=True, max_length=-1)  # Field name made lowercase.
    postedat = models.CharField(db_column='postedAt', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    scheduletype = models.CharField(db_column='scheduleType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    applylinktitle = models.CharField(db_column='applyLinkTitle', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    salary = models.CharField(max_length=-1, blank=True, null=True)
    workfromhome = models.BooleanField(db_column='workFromHome')  # Field name made lowercase.
    responsibilities = models.TextField()  # This field type is a guess.
    qualifications = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'job'


class Qualifications(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'qualifications'
