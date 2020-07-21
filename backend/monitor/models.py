from django.contrib.postgres.fields import JSONField
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100)
    customers = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=100)
    metadata = JSONField(null=True)
    content = models.FileField(upload_to="videos/", null=True)

    def __str__(self):
        return self.name
