from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=150)
    image = models.TextField()
    description = models.TextField()

    @classmethod
    def create(cls, name, image, description):
        movie = cls(name=name, image=image, description=description)
        movie.save()
        return movie

    def __str__(self):
        return self.name
