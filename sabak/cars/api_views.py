from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Car, User
from .serializers import CarSerializer, UserSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]  # Только аутентифицированные пользователи

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Все могут регистрироваться
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]  # Для регистрации разрешаем всем
        return [IsAuthenticated()]  # Для других действий нужна аутентификация