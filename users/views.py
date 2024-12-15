from rest_framework import generics

from users.models import User
from users.permissions import IsActive
from users.serializer import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Создание нового пользователя."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsActive]
    
    def perform_create(self, serializer):
        """Сохраняет нового пользователя с активным статусом."""
        user = serializer.save(is_active_employee=True)
        user.set_password(user.password)
        user.save()
    