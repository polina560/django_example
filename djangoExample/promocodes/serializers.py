from django.contrib.auth.models import User
from rest_framework import serializers

from djangoExample.promocodes.models import Promocode


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User"""

    class Meta:
        model = User
        fields = ('id', 'username')

class PromocodeSerializer(serializers.Serializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Promocode
        fields = ('id', 'code')