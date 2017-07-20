from django.contrib.auth.models import User

from models import *
from serializers import *
from django.shortcuts import get_object_or_404, get_list_or_404


def userLoginRepository(user_serializer):
    print(user_serializer["username"].value)
    user = User.objects.filter(username=user_serializer['username'].value, email=user_serializer['email'].value)
    if not user:
        new_user = UserSerializer(data=user_serializer.data)
        new_user.is_valid(raise_exception=True)
            
        user = new_user.save()
    else:
        user = user.get()
    return UserSerializer(user)

def releasePlayerRepository(players_crud_serializer):
    user_track_query_set = UserCurrentTrack.objects.filter(user=players_crud_serializer['user'].value)
    for user_track in user_track_query_set:
        for player in  user_track.player_list.all():
            if player.id in players_crud_serializer['player_list'].value:
                user_track.player_list.remove(player)
    return UserPlayerSerializer(user_track)

def chatLogRepository(chat_log_serializer):
    chat_log = None
    if chat_log_serializer['type'].value == 'player':
        chat_log = get_list_or_404(ChatLog,user=chat_log_serializer['user'].value, player=chat_log_serializer['type_id'].value)
    elif chat_log_serializer['type'].value == 'manager':
        chat_log = get_list_or_404(ChatLog,user=chat_log_serializer['user'].value, manager=chat_log_serializer['type_id'].value)
    #elif chat_log_serializer['type'].value == 'chairman':
    else:
        chat_log = get_list_or_404(ChatLog,user=chat_log_serializer['user'].value, chairman=chat_log_serializer['type_id'].value)
    return chat_log

def chatRepository(user_chat_serializer):
    chat_data = get_object_or_404(Chat,type=user_chat_serializer['type'].value, message1=user_chat_serializer['message1'].value, message2=user_chat_serializer['message2'].value, message3=user_chat_serializer['message3'].value, message4=user_chat_serializer['message4'].value)
    return BotChatSerializer(chat_data)
