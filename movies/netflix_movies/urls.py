from rest_framework import routers
from .views import MovieList, MovieDetail, VoteList
from django.urls import include, path


urlpatterns = [
    path(r'api/', MovieList.as_view(), name="movie-list"),
    path(r'api/<pk>', MovieDetail.as_view(), name="movie-detail"),
    path(r'api/vote/', VoteList.as_view(), name="vote-list")
    ]