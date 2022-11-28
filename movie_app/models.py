from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def movies_count(self):
        return self.movies.all().count()


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=30)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='movies')

    def __str__(self):
        return self.title

    def rating(self):
        arr = [rate.stars for rate in self.reviews.all()]
        return sum(arr) / len(arr) if len(arr) != 0 else 'No rating'


MY_RATING = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(default=1, choices=MY_RATING)
