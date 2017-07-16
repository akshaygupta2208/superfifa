from django.contrib.auth.models import User

from serializers import UserSerializer
from models import UserCurrentTrack
from serializers import UserPlayerSerializer


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
