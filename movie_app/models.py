from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=30)
    director = models.ForeignKey(Director, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)