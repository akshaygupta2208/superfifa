from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from models import *
from serializers import *
from services import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.settings import api_settings


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
        "email": "someemail",
        "first_name": "firstname",
        "last_name": "lastname"
        }
    """
    def post(self, request, format=None):
        user_serializer = UserSerializer(request.data)
        response = userLoginService(user_serializer)
        
        return JsonResponse(response)
    

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

class UserPlayerListViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for viewing PlayerList.
    """
    queryset = UserCurrentTrack.objects.all()
    serializer_class = UserPlayerSerializer
    
class ReleasePlayerView(APIView):
    """
        Service Release Player 
        -------------------
        This Api can be used to release a player from agency use options to see the api end points
        -------------------
        request format : 
        {"user":1,"player_list":[1,3,4]}
    """
    def post(self, request, format=None):
        players_crud_serializer = PlayerCRUDSerializer(request.data)
        response = releasePlayerService(players_crud_serializer)
        return JsonResponse(response)

class ChatView(APIView):
    """
        Service Release Player 
        -------------------
        This Api can be used to get chat response use options to see the api end points
        -------------------
        request format : 
        {"user":1,"player_list":[1,3,4]}
    """
    def post(self, request, format=None):
        user_chat_serializer = UserChatSerializer(request.data)
        response = chatService(user_chat_serializer, request.user)
        return JsonResponse(response)

class ChatLogView(APIView):
    """
        Service Chat Logs 
        -------------------
        This Api can be used to get chat logs use options to see the api end points
        -------------------
        request format : 
        {"user":3,"type_id":1, "type":"player"}
    """
    def post(self, request, format=None):
        chat_log_serializer = ChatLogDTOSerializer(data = request.data)
        chat_log = ChatLogService(chat_log_serializer)
        pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
        paginator = pagination_class()
        page = paginator.paginate_queryset(chat_log, request)
        serializer = ChatLogSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
        
        
