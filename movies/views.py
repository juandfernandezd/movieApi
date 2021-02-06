from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from movies.models import Movie
from movies.serializers import MovieSerializer


# Create your views here.
class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]
