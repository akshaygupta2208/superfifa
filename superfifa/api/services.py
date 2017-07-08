from django.contrib.auth.models import User
from serializers import UserSerializer
from repository import userLoginRepository



def userLoginService(user_serializer):
    user = userLoginRepository(user_serializer)
    return user.data
