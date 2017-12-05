from django.db import models


# Create your models here.

class Influencer(models.Model):
    object_url_id = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    register_date = models.DateField(blank=True, null=True)
    subscriber_count = models.IntegerField(blank=True, null=True, default=0)
    view_count = models.IntegerField(blank=True, null=True, default=0)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
