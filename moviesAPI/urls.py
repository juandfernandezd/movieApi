from django.urls import path, include
from moviesAPI import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'scores', views.ScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
