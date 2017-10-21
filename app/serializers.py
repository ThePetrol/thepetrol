from app.models import Message, Animal
from rest_framework import serializers

class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animal
        fields = ('url', 'username', 'email', 'groups')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = (
            'text',
            'created',
            'updated',
            'from_number',
            'to_number',
            'sent',
            'received',
            'error',
            'text',
        )