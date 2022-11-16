from rest_framework import serializers
from .models import Movie, Tmdb_Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# 영화 상세정보
class MovieSerializerTMDB(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Tmdb_Movie
        fields = '__all__'


# 영화 전체 리스트
class MovieListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Tmdb_Movie
        fields = '__all__'
