from django.db import models

from api.models.movie_models import Movie

class Actor(models.Model):
    name = models.CharField(max_length=256)
    movies = models.ManyToManyField(Movie)
