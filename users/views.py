from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """ Отвечает за создание сущности (Generic-класс)"""

    serializer_class = UserSerializer
    queryset = User.objects.all()

