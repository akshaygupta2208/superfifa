from django.contrib.auth.models import User
from serializers import UserSerializer
from repository import *



def userLoginService(user_serializer):
    user = userLoginRepository(user_serializer)
    return user.data


def releasePlayerService(players_crud_serializer):
    player_crud_result = releasePlayerRepository(players_crud_serializer)
    return player_crud_result.data

def ChatLogService(chat_log_serializer):
    chat_log_serializer.is_valid()
    chat_log_query_set = chatLogRepository(chat_log_serializer)
    return chat_log_query_set

def chatService(user_chat_serializer, user):
    chat_data = chatRepository(user_chat_serializer, user)
    return chat_data.data