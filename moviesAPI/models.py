from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    image_path = models.TextField(default='')
    description = models.TextField(default='')

    @classmethod
    def create(cls, title, image_path, description):
        movie = cls(title=title, image_path=image_path, description=description)
        movie.save()
        return movie

    def __str__(self):
        return self.name


class Score(models.Model):
    points = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='scores')

    @classmethod
    def create(cls, points, movie):
        score = cls(points=points, movie=movie)
        score.save()
        return score

    def __str__(self):
        return self.movie.title + ' ' + self.points
