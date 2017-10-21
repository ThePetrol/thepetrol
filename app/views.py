from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from app.serializers import MessageSerializer, AnimalSerializer
from app.models import Message, Animal


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer