from api.models.movie_models import Movie


class SlowDataRepository:
    def __init__(self):
        self.data = Movie.objects.all()
        
    def execute(self):
        print('slow_list')
        data_set = []
        search_actor = 'Arnold S.'
        for movie in self.data:
            for actor in movie.actor_set.all():
                if actor.name == search_actor:
                    print(f'{movie.title} has actor: {search_actor}')
                    data_set.append(movie)
                
        return [{'title': data.title, 'description': data.description} for data in data_set]
