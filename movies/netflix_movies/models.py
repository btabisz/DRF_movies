from django.db import models


class Category(models.Model):
    category_name = models.TextField(default=None)

    def __str__(self):
        return self.category_name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.title


class Vote(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    vote = models.IntegerField()
    reason = models.TextField(max_length=100)

    def __str__(self):
        return ""

