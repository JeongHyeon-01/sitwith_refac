from .models import User
from .serializer import SignupSirializer, SigninSirializer

from rest_framework import generics, status
from rest_framework.response import Response

from utils.decorator import login_authorization

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSirializer

class SigninView(generics.GenericAPIView):
    serializer_class = SigninSirializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        token = serializer.validated_data
        response = Response(
                {
                    "user": token['user'],
                    "message": "login success",
                    "jwt_token": {
                        "access_token": token['access_token'],
                        "refresh_token": token['refresh_token'],
                    },
                },
                status=status.HTTP_200_OK
            )
        response.set_cookie("access_token", token['access_token'], httponly=True)
        response.set_cookie("refresh_token", token['refresh_token'], httponly=True)
        return response


class HelloView(generics.GenericAPIView):
    @login_authorization    
    def get(self, request):
        return Response("Hello",status=status.HTTP_200_OK)