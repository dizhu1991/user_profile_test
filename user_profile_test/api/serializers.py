from rest_framework.serializers import ModelSerializer

from user_profile_test.models import MyUser


class MyUserSerializer(ModelSerializer):
    """Serializes MyUser object."""
    class Meta:
        model = MyUser
        exclude = ['password', ]
