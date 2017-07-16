from django.contrib.auth.models import User
from serializers import UserSerializer
from repository import *



def userLoginService(user_serializer):
    user = userLoginRepository(user_serializer)
    return user.data


def releasePlayerService(players_crud_serializer):
    player_crud_result = releasePlayerRepository(players_crud_serializer)
    return player_crud_result.data