from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
