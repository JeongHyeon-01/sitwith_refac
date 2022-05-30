from django.db import models

class TimeStampZone(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_time = models.DateTimeField(null=True)