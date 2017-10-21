from app.models import Message, Animal, Shelter
from rest_framework import serializers

class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ShelterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shelter
        fields = '__all__'
