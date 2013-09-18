from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Complaints(models.Model):
    latitude = models.FloatField(max_length=20, null=True)
    longitude = models.FloatField(max_length=20, null=True)
    opened = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)
    supervisor_district = models.IntegerField(max_length=2, null=True)
    status = models.CharField(max_length=255, blank=True)
    case_id = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    request_details = models.CharField(max_length=255, blank=True)
    neighborhood = models.CharField(max_length=255, blank=True)

    class Meta:
        app_label = "app"

class Comments(models.Model):
    complaints = models.ForeignKey(Complaints, related_name="comments")
    user = models.ForeignKey(User)
    comments_date = models.DateTimeField(null=True, auto_now_add=True)
    comments_created_date = models.DateTimeField(null=True, auto_now=True)
    comments = models.TextField(blank=True)

    class Meta:
        app_label = "app"


#    def __unicode__(self):
#       return self.address

"""
class User(models.Model):
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255)
    date_created = models.DateTimeField(null=True)

    class Meta:
        app_label="app"
"""