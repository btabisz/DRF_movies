from .models import Movie, Category, Vote
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'category', 'description']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['movie', 'vote', 'reason']
        depth = 1

