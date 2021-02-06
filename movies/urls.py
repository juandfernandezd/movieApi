from django.urls import path, include
from movies import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
