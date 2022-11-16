from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie, Tmdb_Movie
from .serializers import MovieListSerializer, MovieSerializerTMDB

@api_view(['GET'])
def movie_list(request):
    movies = Tmdb_Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Tmdb_Movie.objects.get(movie_id=movie_pk)
    serializer = MovieSerializerTMDB(movie)
    return Response(serializer.data)