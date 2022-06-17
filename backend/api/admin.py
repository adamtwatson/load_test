
from django.contrib import admin

from api.models.actor_models import Actor
from api.models.movie_models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(Movie, MovieAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    raw_id_fields = ('movies', )

admin.site.register(Actor, ActorAdmin)