from api.models.movie_models import Movie
from api.models.actor_models import Actor


class FastDataRepository:

    def __init__(self):
        # self.data = Movie.objects.all().prefetch_related('actor_set')
        pass
        
    def execute(self):
        # data_set = []
        return self.execute_faster()
        # search_actor = 'Arnold S.'
        # for movie in self.data:
        #     for actor in movie.actor_set.all():
        #         if actor.name == search_actor:
        #             print(f'{movie.title} has actor: {search_actor}')
        #             # data_set.append(movie)
        #             yield {'title': movie.title, 'description': movie.description}
        #             break
        # 
        # return [{'title': data.title, 'description': data.description} for data in data_set]
    
    @staticmethod
    def execute_faster():
        # find the actor first, then yield the movies
        print('fast_list')
        actor = Actor.objects.filter(name='Arnold S.').first()
        for movie in actor.movies.all():
            yield {'title': movie.title, 'description': movie.description}