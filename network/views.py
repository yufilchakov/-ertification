from rest_framework import viewsets, permissions

from network.models import Contacts, Network, Product
from network.serializer import ContactsSerializer, NetworkSerializer, ProductSerializer
from users.permissions import IsActive


class ContactsViewSet(viewsets.ModelViewSet):
    """Представление для модели Contacts."""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsActive]


class NetworkViewSet(viewsets.ModelViewSet):
    """Представление для модели Network."""
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]

    def perform_update(self, serializer):
        """Запретить обновление поля 'debt' через API."""
        serializer.save(debt=self.get_object().debt)


class ProductViewSet(viewsets.ModelViewSet):
    """Представление для модели Product."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
