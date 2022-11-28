from rest_framework import serializers
from .models import Director, Movie, Review


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

    def get_movies_count(self, director):
        return director.movies_count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title rating description duration director reviews'.split()

    def get_rating(self, movie):
        return movie.rating()
