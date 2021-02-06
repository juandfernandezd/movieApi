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
