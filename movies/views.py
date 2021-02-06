from rest_framework.viewsets import ModelViewSet
from movies.models import Movie
from movies.serializers import MovieSerializer


# Create your views here.
class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
