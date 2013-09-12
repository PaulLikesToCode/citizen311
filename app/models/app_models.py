from django.db import models

class Complaints(models.Model):
    latitude = models.IntegerField(max_length= 20)
    longitude = models.IntegerField(max_length= 20)
    opened = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)
    supervisor_district = models.IntegerField(max_length=2)
    status = models.CharField(max_length=255)
    case_id = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    request_details = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    comments_date = models.DateTimeField(null=True)
    comments_created_date = models.DateTimeField
    comments = models.CharField(max_length=None)

class User(models.Model):
    id = models.ForeignKey('Complaints')
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255)
    date_created = models.DateTimeField(null=True)