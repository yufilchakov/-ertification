from rest_framework import serializers

from network.models import Contacts, Network, Product


class ContactsSerializer(serializers.ModelSerializer):
    """Реализация сериализатора для модели Contacts."""
    
    class Meta:
        model = Contacts
        fields = '__all__'
        read_only_fields = ['id']


class NetworkSerializer(serializers.ModelSerializer):
    """Реализация сериализатора для модели Network."""
    
    class Meta:
        model = Network
        fields = '__all__'
        read_only_fields = ['id', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    """Реализация сериализатора для модели Product."""
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id']
