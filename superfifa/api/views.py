from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from ml.test_predict import get_prediction
from serializers import UserSerializer


class APIRoot(generics.GenericAPIView):
    """
    Super Fifa API documentation
    """

    def get(self, request):
        return Response({
            "create_user": "http://localhost:8000/create_user",
            "update_user": "http://localhost:8080/user_details/1",
            "user_login": "http://localhost:8080/user_login"
        })


class UserCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
        Service User Registration
        --------------------------
        This api is used to user registration use options to see the api end points
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
        Service User Detail 
        -------------------
        This Api can be used to update User data and get user basic details use options to see the api end points
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(APIView):
    """
        Service User Login 
        -------------------
        This Api can be used for user login and get user basic details use options to see the api end points
        -------------------
        request format : 
        {
        "username": "someusername",
        "email": "someemail"
        }
    """

    def get_object(self, username, email):
        try:
            return User.objects.get(username=username, email=email)
        except User.DoesNotExist:
            raise PermissionDenied

    def post(self, request, format=None):
        get_prediction()
        serializer = UserSerializer(request.data)
        user = self.get_object(
            serializer['username'].value, serializer['email'].value)
        serializer = UserSerializer(user)
        return Response(serializer.data)


"""
    Service Get My Player List  
 
    ------------
    TODO: Implement it later
"""
"""
    Service Release My Player 
 
    ------------
    TODO: Implement it later
"""
