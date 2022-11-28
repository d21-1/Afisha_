from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer
from .models import Director, Movie, Review
from rest_framework import status


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'}, status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(director).data
    return Response(data=serializer)


@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie does not exists!'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie).data
    return Response(data=serializer)


@api_view(['GET'])
def reviews_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'No review!'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review).data
    return Response(data=serializer)


@api_view(['GET'])
def movies_reviews_view(request):
    movies = Movie.objects.all()
    serializer = MovieReviewSerializer(movies, many=True)
    return Response(data=serializer.data)
