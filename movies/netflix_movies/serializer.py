from .models import Movie, Category, Vote
from rest_framework import serializers


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'category', 'description']


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ['movie', 'vote', 'reason']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']
