from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import *

from users.serializers import UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    user_id = request.data.get('user_id')
    password = request.data.get('password')
    if User.objects.filter(user_id=user_id).exists():
        return Response({'message' : '이 아이디는 이미 사용중이여라...'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password) #패스워드를 db에 저장하지않기때문에 따로 저장하는것임.
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    user_id = request.data.get('user_id')
    password = request.data.get('password')

    user = authenticate(user_id=user_id, password=password)  #로그인했을때 db에 있는 값과 일치하는지 확인
    if user is None:
        return Response({'message': '아이디 또는 비밀번호가 일치하지 않아요!!!'}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    update_last_login(None, user)

    return Response({'refresh_token': str(refresh),
                     'access_token': str(refresh.access_token), }, status=status.HTTP_200_OK)