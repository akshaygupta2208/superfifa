from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from serializers import UserSerializer


class UserCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
        Service User Register 

        ------------
        TODO: Implement it later
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
        Service User deactivate 

        ------------
        TODO: Implement it later

        Service User activate 

        ------------
        TODO: Implement it later
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(APIView):

    def get_object(self, username, email):
        try:
            return User.objects.get(username=username, email=email)
        except User.DoesNotExist:
            raise PermissionDenied

    def post(self, request, format=None):
        serializer = UserSerializer(request.data)
        user = self.get_object(
            serializer['username'].value, serializer['email'].value)
        serializer = UserSerializer(user)
        return Response(serializer.data)


"""
    Service User login 
 
    ------------
    TODO: Implement it later
"""

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
