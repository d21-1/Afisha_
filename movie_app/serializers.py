from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


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
        fields = 'id text stars movie'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title rating description duration director reviews'.split()

    def get_rating(self, movie):
        return movie.rating()


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=30)
    description = serializers.CharField(min_length=10, max_length=1000)
    duration = serializers.CharField(min_length=1, max_length=10)
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director does not exists!')
        return director_id

    def validate_title(self, title):
        if not Movie.objects.filter(title=title).exists():
            return title
        else:
            raise ValidationError('Movie already exists!')


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=15)

    def validate_name(self, name):
        if not Director.objects.filter(name=name).exists():
            return name
        else:
            raise ValidationError('Director already exists!')


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=5, max_length=150)
    movie_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Movie does not exists!')
        return movie_id
