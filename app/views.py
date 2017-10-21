from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from app.serializers import MessageSerializer, AnimalSerializer, ShelterSerializer
from app.models import Message, Animal, Shelter
from rest_framework.decorators import api_view
from django.http import HttpResponse, Http404
from django.conf import settings
from django.views.generic import TemplateView

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

class ShelterViewSet(viewsets.ModelViewSet):

    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

@api_view()
def locate(request):
    lat = request.GET.get("lat")
    lng = request.GET.get("lng")


    if not lat or not lng:
        raise Http404

    if settings.DEBUG:
        return HttpResponse(settings.DEBUG_PHONE_NUMBER)

    lat_lng = {
        'lat': lat,
        'lng': lng,
    }

    # Create the query
    query = 'Animal rescue shelter'
    from googleplaces import GooglePlaces, ranking
    # Query for closest shelter
    google = GooglePlaces(api_key=settings.GOOGLE_API_KEY)
    result = google.nearby_search(lat_lng=lat_lng, name=query, rankby=ranking.DISTANCE)

    # Get nearest animal shelter with available phone number
    for shelter in result.places:
        shelter.get_details()
        if shelter.local_phone_number:
            return HttpResponse(shelter.local_phone_number)

    raise Http404