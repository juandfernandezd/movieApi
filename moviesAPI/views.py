from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from moviesAPI.models import Movie, Score
from moviesAPI.serializers import MovieSerializer, ScoreSerializer
from django.db.models import Avg, F


# Create your views here.
class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().annotate(avg_rating=Avg(F('scores__points')))


class ScoreViewSet(ModelViewSet):
    queryset = Score.objects.all().order_by('id')
    serializer_class = ScoreSerializer
    filter_fields = ('movie__id',)
    permission_classes = [permissions.IsAuthenticated]
