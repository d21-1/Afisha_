from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import UserCreateSerializer, UserValidateSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def register_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(**serializer.validated_data)
    return Response(status=status.HTTP_201_CREATED,
                    data={'message': 'User created!'})


@api_view(['POST'])
def authorize_view(request):
    serializer = UserValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED,
                        data={'message': 'User credentials are wrong!'})
    token, created = Token.objects.get_or_create(user=user)
    return Response(data={'key': token.key})
