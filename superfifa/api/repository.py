from django.contrib.auth.models import User

from serializers import UserSerializer


def userLoginRepository(user_serializer):
    print(user_serializer["username"].value)
    user = User.objects.filter(username=user_serializer['username'].value,email=user_serializer['email'].value)
    if not user:
        new_user= UserSerializer(data=user_serializer.data)
        new_user.is_valid(raise_exception=True)
            
        user = new_user.save()
    else:
        user = user.get()
    return UserSerializer(user)

