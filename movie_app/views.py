from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer, \
    MovieValidateSerializer, DirectorValidateSerializer, ReviewValidateSerializer
from .models import Director, Movie, Review
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


class DirectorModelViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    lookup_field = 'id'


class MovieModelViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    lookup_field = 'id'


class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    lookup_field = 'id'


# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def directors_view(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         serializer = DirectorSerializer(directors, many=True)
#         return Response(data=serializer.data)
#     else:
#         serializer = DirectorValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         name = serializer.validated_data['name']
#         director = Director.objects.create(name=name)
#         director.save()
#         return Response(status=status.HTTP_201_CREATED,
#                         data={
#                             'message': 'director added',
#                             'director': DirectorSerializer(director).data
#                         })
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def director_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(data={'error': 'Director not found!'}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = DirectorSerializer(director).data
#         return Response(data=serializer)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'director removed'})
#     elif request.method == 'PUT':
#         serializer = DirectorValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         director.name = serializer.validated_data['name']
#         director.save()
#         return Response(data={
#                             'message': 'director updated',
#                             'director': DirectorSerializer(director).data
#                         })
#
#
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def movies_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data)
#     else:
#         serializer = MovieValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'errors': serializer.errors})
#         title = serializer.validated_data['title']
#         description = serializer.validated_data['description']
#         duration = serializer.validated_data['duration']
#         director_id = serializer.validated_data['director_id']
#         movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
#         movie.save()
#         return Response(status=status.HTTP_201_CREATED,
#                         data={
#                             'message': 'movie added',
#                             'movie': MovieSerializer(movie).data
#                         })
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def movie_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data={'error': 'Movie does not exists!'}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie).data
#         return Response(data=serializer)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'movie deleted'})
#     elif request.method == 'PUT':
#         serializer = MovieValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movie.title = serializer.validated_data.get('title')
#         movie.description = serializer.validated_data.get('description')
#         movie.duration = serializer.validated_data.get('duration')
#         movie.director_id = serializer.validated_data.get('director_id')
#         movie.save()
#         return Response(data={
#             'message': 'movie updated',
#             'director': MovieSerializer(movie).data
#         })
#
#
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def reviews_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(data=serializer.data)
#     else:
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         text = serializer.validated_data['text']
#         movie_id = serializer.validated_data['movie_id']
#         stars = serializer.validated_data['stars']
#         review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
#         review.save()
#         return Response(status=status.HTTP_201_CREATED,
#                         data={
#                             'message': 'review created',
#                             'movie': ReviewSerializer(review).data
#                         })
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def review_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'error': 'No review!'}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = ReviewSerializer(review).data
#         return Response(data=serializer)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'review deleted'})
#     elif request.method == 'PUT':
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         review.text = serializer.validated_data['text']
#         review.movie_id = serializer.validated_data['movie_id']
#         review.stars = serializer.validated_data['stars']
#         review.save()
#         return Response(data={
#             'message': 'review updated',
#             'director': ReviewSerializer(review).data
#         })
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def movies_reviews_view(request):
#     movies = Movie.objects.all()
#     serializer = MovieReviewSerializer(movies, many=True)
#     return Response(data=serializer.data)
