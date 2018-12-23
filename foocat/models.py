from django.db import models

# Create your models here.

class Device(models.Model):
    did = models.CharField(max_length=40)
    name = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        db_table = 'device'
