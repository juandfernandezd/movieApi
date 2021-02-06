from moviesAPI.models import Movie, Score
from rest_framework.serializers import ModelSerializer
from rest_framework import  serializers


class MovieSerializer(ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'image_path', 'description', 'avg_rating')


class ScoreSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = ('points', 'movie',)
