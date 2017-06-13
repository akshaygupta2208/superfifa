

from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from ml.test_predict import get_prediction
from models import *
from serializers import *


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
        league = League()
        league.image_url = "/static/league1.png"
        league.name = "barclays premier league"
        league.rating = 4
        league.save()
        serializer = UserSerializer(request.data)
        user = self.get_object(
            serializer['username'].value, serializer['email'].value)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LeagueViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Leagues.
    """
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Teams.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ChairmanViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Chairmans.
    """
    queryset = Chairman.objects.all()
    serializer_class = ChairmanSerializer


class ScoutViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Scouts.
    """
    queryset = Scout.objects.all()
    serializer_class = ScoutSerializer


class CoachViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Coaches.
    """
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class OfficeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Offices.
    """
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Players.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class MediaCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Media Companies.
    """
    queryset = MediaCompany.objects.all()
    serializer_class = MediaCompanySerializer


class JournalistViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Journalists.
    """
    queryset = Journalist.objects.all()
    serializer_class = JournalistSerializer


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing News.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer


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
