from django.contrib.auth.models import User

from models import *
from serializers import *
from django.shortcuts import get_object_or_404, get_list_or_404


def add_dummy_players(user):
    user_track = UserCurrentTrack()
    user_track.user = user
    user_track.save()
    player_list = Player.objects.all()
    for player in player_list:
        user_track.player_list.add(player)
    user_track.save()
    pass



def userLoginRepository(user_serializer):
    print(user_serializer["username"].value)
    user = User.objects.filter(username=user_serializer['username'].value, email=user_serializer['email'].value)
    if not user:
        new_user = UserSerializer(data=user_serializer.data)
        new_user.is_valid(raise_exception=True)        
        user = new_user.save()
        add_dummy_players(user)
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
    if chat_log_serializer['type'].value == 'P':
        chat_log = get_list_or_404(ChatLog, user=chat_log_serializer['user'].value, player=chat_log_serializer['type_id'].value)
    elif chat_log_serializer['type'].value == 'M':
        chat_log = get_list_or_404(ChatLog, user=chat_log_serializer['user'].value, manager=chat_log_serializer['type_id'].value)
    # elif chat_log_serializer['type'].value == 'chairman':
    elif chat_log_serializer['type'].value == 'C':
        chat_log = get_list_or_404(ChatLog, user=chat_log_serializer['user'].value, chairman=chat_log_serializer['type_id'].value)
    return chat_log


def save_chat_log(actor, message , user, type, type_id):
    # actor for YOU is zero and for bot it is one
    log = ChatLog()
    log.actor = actor
    log.message = message
    log.user = User.objects.get(pk=user)
    
    if type == 'P':
        log.player = Player.objects.get(pk=type_id)
        
    elif type == 'M':
        log.player = Manager.objects.get(pk=type_id)
    elif type == 'C':
        log.player = Chairman.objects.get(pk=type_id)
    log.save()

def chatRepository(user_chat_serializer, user, mode):
    """
    save the reply latest reply in chat log
    mode = 1 is read mode
    """
    if mode == 1: 
        if user_chat_serializer['message4'].value != '-':
            save_chat_log(ChatLog.ACTOR_TYPE[0][0], user_chat_serializer['message4'].value, user, user_chat_serializer['type'].value, user_chat_serializer['type_id'].value['type_id'])
        elif user_chat_serializer['message3'].value != '-':   
            save_chat_log(ChatLog.ACTOR_TYPE[0][0], user_chat_serializer['message3'].value, user, user_chat_serializer['type'].value, user_chat_serializer['type_id'].value['type_id'])
        elif user_chat_serializer['message2'].value != '-':
            save_chat_log(ChatLog.ACTOR_TYPE[0][0], user_chat_serializer['message2'].value, user, user_chat_serializer['type'].value, user_chat_serializer['type_id'].value['type_id'])
        elif user_chat_serializer['message1'].value != '-':
            save_chat_log(ChatLog.ACTOR_TYPE[0][0], user_chat_serializer['message1'].value, user, user_chat_serializer['type'].value, user_chat_serializer['type_id'].value['type_id'])               
    
    """
    get chat responses
    """    
    chat_data = get_object_or_404(Chat, type=user_chat_serializer['type'].value, message1=user_chat_serializer['message1'].value, message2=user_chat_serializer['message2'].value, message3=user_chat_serializer['message3'].value, message4=user_chat_serializer['message4'].value)
    """
    if it is the first interaction then check if the response 
    is there or not an if response is there then update the log
    """
    if chat_data.reply != '-' and mode == 1:
        save_chat_log(ChatLog.ACTOR_TYPE[1][0], chat_data.reply, user, user_chat_serializer['type'].value, user_chat_serializer['type_id'].value['type_id'])
        
    return BotChatSerializer(chat_data)








