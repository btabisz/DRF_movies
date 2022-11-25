from django.contrib import admin
from .models import Movie, Vote, Category


class VoteInLine(admin.TabularInline):
    model = Vote


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']
    inlines = [VoteInLine]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'vote', 'reason']
