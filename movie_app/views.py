from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer
from .models import Director, Movie, Review
from rest_framework import status


@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    else:
        name = request.data.get('name', None)
        director = Director.objects.create(name=name)
        director.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={
                            'message': 'director added',
                            'director': DirectorSerializer(director).data
                        })


@api_view(['GET', 'PUT', 'DELETE'])
def director_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director).data
        return Response(data=serializer)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'director removed'})
    elif request.method == 'PUT':
        name = request.data.get('name', None)
        director.name = name
        director.save()
        return Response(data={
                            'message': 'director updated',
                            'director': DirectorSerializer(director).data
                        })


@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    else:
        title = request.data.get('title', None)
        description = request.data.get('description', None)
        duration = request.data.get('duration', None)
        director_id = request.data.get('director', None)
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={
                            'message': 'movie added',
                            'movie': MovieSerializer(movie).data
                        })


@api_view(['GET', 'PUT', 'DELETE'])
def movie_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie does not exists!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie).data
        return Response(data=serializer)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'movie deleted'})
    elif request.method == 'PUT':
        title = request.data.get('title', None)
        description = request.data.get('description', None)
        duration = request.data.get('duration', None)
        director_id = request.data.get('director', None)
        movie.title = title
        movie.description = description
        movie.duration = duration
        movie.director_id = director_id
        movie.save()
        return Response(data={
            'message': 'movie updated',
            'director': MovieSerializer(movie).data
        })


@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    else:
        text = request.data.get('text', None)
        movie_id = request.data.get('movie_id', None)
        stars = request.data.get('stars', 1)
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={
                            'message': 'review created',
                            'movie': ReviewSerializer(review).data
                        })


@api_view(['GET', 'PUT', 'DELETE'])
def review_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'No review!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review).data
        return Response(data=serializer)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'review deleted'})
    elif request.method == 'PUT':
        text = request.data.get('text', None)
        movie_id = request.data.get('movie_id', None)
        stars = request.data.get('stars', 1)
        review.text = text
        review.movie_id = movie_id
        review.stars = stars
        review.save()
        return Response(data={
            'message': 'review updated',
            'director': ReviewSerializer(review).data
        })


@api_view(['GET'])
def movies_reviews_view(request):
    movies = Movie.objects.all()
    serializer = MovieReviewSerializer(movies, many=True)
    return Response(data=serializer.data)
