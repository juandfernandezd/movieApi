from decouple import config
from moviesAPI.models import Movie
from random import randint
import requests

API_KEY = config('API_KEY')
BASE_URL = 'https://api.themoviedb.org/3'
BASE_IMAGE_PATH = 'https://image.tmdb.org/t/p/w500'


def insert_movie(row_movie):
    # id = row_movie['id']
    title = row_movie['original_title']
    image_path = '{0}/{1}'.format(BASE_IMAGE_PATH, row_movie['backdrop_path'])
    description = row_movie['overview']
    Movie.create(title, image_path, description)


def get_movies():
    page = randint(1, 500)
    url = '''{0}/discover/movie?api_key={1}&language=en-US&sort_by=popularity.desc&include_adult=false
             &include_video=false&page={2}'''.format(BASE_URL, API_KEY, page)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        movies = data['results']

        for movie in movies:
            insert_movie(movie)

