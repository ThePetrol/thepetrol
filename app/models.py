from __future__ import unicode_literals
from common import enum
from django.db import models
#
# from django.contrib.postgres.fields import JSONField, ArrayField

class Color(enum.Enum):
    black = enum.Item(1, "Black")
    brown = enum.Item(2, "Brown")
    orange = enum.Item(3, "Orange")

class AnimalType(enum.Enum):
    dog = enum.Item(1, "Dog")
    cat = enum.Item(2, "Cat")

class Pattern(enum.Enum):
    spotted = enum.Item(1, "Spotted")
    striped = enum.Item(2, "Striped")
    calico = enum.Item(3, "Calido")
    solid = enum.Item(4, "Solid")

class BreedType(enum.Enum):
    # there are < 400 breeds of dog in the world
    goldem_retreiver = enum.Item(1, "Golden Retriever")



class DogBreedGroup(enum.Enum):
    # https://www.psychologytoday.com/blog/canine-corner/201305/how-many-breeds-dogs-are-there-in-the-world


    #Sheepdogs and Cattle Dogs other than Swiss Cattle Dogs (this group includes most of the dogs found classified as "herding dogs" by other kennel clubs).
    herding = enum.Item(1, "Herding")
    # Pinscher and Schnauzer - Molossoid Breeds - Swiss Mountain and Cattle Dogs and Other Breeds (the Molossian breeds include the dogs known as the mastiffs by most other kennel clubs)
    molosser  = enum.Item(2, "Molosser")
    # Terriers
    terrier = enum.Item(3, "Terrier")
    # Dachshunds
    dachsund = enum.Item(4, "Dachsund")
    # Spitz and Primitive Types
    spitz = enum.Item(5, "Spitz")

    # Scenthounds and Related Breeds
    scenthound = enum.Item(6, "Scenthound")
    # Pointers and Setters
    pointer = enum.Item(7, "Pointer")
    # Retrievers - Flushing Dogs - Water Dogs
    retreiver = enum.Item(8, "Retriever")
    # Companion and Toy Dogs
    companion  = enum.Item(9, "Companion")
    # Sighthounds
    sighthound = enum.Item(10, "Sighthound")

class CatBreedGroup(enum.Enum):
    pass


class Size(enum.Enum):
    small = enum.Item(1, "Small")
    medium = enum.Item(2, "Medium")
    large = enum.Item(3, "Large")

# Create your models here.
class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
#
class Message(TimeStamp):
    '''
    Represents a message that was sent or received via twilio
    '''
    from_number = models.IntegerField()
    to_number = models.IntegerField()
    # was there an error in sending this message
    error = models.BooleanField(default=False)
    # animal = models.ForeignKey(Animal, blank=True, null=True, related_name="messages")

    # the text tha was received
    text = models.CharField(max_length=2048)

    # the response that was generated
    response = models.CharField(max_length=2048, blank=True, null=True)

nullable = {"blank": True, "null":True}

class EmotionType(enum.Enum):
    angry = enum.Item(1, "Angry")
    scared = enum.Item(2, "Scared")
    aloof = enum.Item(3, "Aloof")
    friendly = enum.Item(4, "Friendly")

class Gender(enum.Enum):
    male = enum.Item(1, "Male")
    female = enum.Item(2, "Female")

import random



points = [
    (38.8977, -77.0365),
    (38.907327, -77.079246),
    (38.910512, -77.079414),
    (38.912251, -77.080579),
    (38.915788, -77.081995),
    (38.920474, -77.083796),
    (38.918002, -77.079870),
    (38.918148, -77.077054),
    (38.924499, -77.082947),
    (38.926065, -77.015119),
    # (40.7829, -73.9654)
    #
]

class Animal(TimeStamp):


    @staticmethod
    def point_near(lat, lng):
        return (
            random.uniform(float(lat) - 0.001, float(lat) + 0.001),
            random.uniform(float(lng) - 0.001, float(lng) + 0.001)
        )

    @staticmethod
    def scatter_around(point):
        points = [point]
        lat, lng = point
        number_of_points = random.randint(5, 10)

        for i in range(number_of_points):
            points.append(Animal.point_near(lat, lng))
        return points

    @staticmethod
    def scatter_animals():
        for point in points:
            surrounding_points = Animal.scatter_around(point)
            for lat, lng in surrounding_points:
                a = Animal(
                    latitude=lat,
                    longitude=lng
                )
                print "Saving", a
                a.save()
    def save(self, **kwargs):
        # if this is the first save
        if not self.pk:
            if self.latitude and self.longitude:
                # scatter near this point
                new_lat, new_lng = Animal.point_near(self.latitude, self.longitude)
                self.latitude = new_lat
                self.longitude = new_lng
        super(Animal, self).save(**kwargs)


    # def scatter_animals(self, latitude, longitude):
    #     # print(Animal.objects.scatter_animals(40.7829, -73.9654)) # Coordinates of Central Par in NYC
    #     animal = self.create(latitude=latitude, longitude=longitude)
    #     animal.latitudes, animal.longitudes = get_distribution(latitude, longitude)
    #     animal.save()
    #     return animal

    # def get_distribution(latitude, longitude):
    #     latitudes = list()
    #     longitudes = list()

    #     for i in range(number_of_points):

    #     return latitudes, longitudes
    # has_tag = models.BooleanField()

    # the size of the animal
    # size = models.IntegerField(choices=Size, default=Size.small)
    size = models.CharField(max_length=255, blank=True, null=True)
    breed = models.CharField(max_length=255, **nullable)
    # breed = models.IntegerField(choices=Breed, **nullable)

    color = models.CharField(max_length=255, **nullable)

    dirty = models.CharField(max_length=255, **nullable)
    # clean = models.CharField(max_length=255, **nullable)

    emotion = models.CharField(max_length=255, **nullable)
    # emotion_type = models.IntegerField(choices=EmotionType, **nullable)

    # gender = models.IntegerField(choices=Gender, **nullable)
    gender = models.CharField(max_length=255, **nullable)

    hair_condition = models.CharField(max_length=255, **nullable)
    health = models.CharField(max_length=255, **nullable)

    pattern = models.CharField(max_length=255, **nullable)
    size = models.CharField(max_length=255, **nullable)
    species = models.CharField(max_length=255, **nullable)
    weight = models.CharField(max_length=255, **nullable)



    # color = models.IntegerField(choices=Color, default=Color)
    # animal_type = models.IntegerField(choices=AnimalType)
    # pattern = models.IntegerField(choices=Pattern)
    # breed = models.CharField(max_length=255)
    # breed_type = models.IntegerField(choices=BreedType)
    # dog_breed_group = models.IntegerField(choices=DogBreedGroup, blank=True, null=True)
    # cat_breed_group = models.IntegerField(choices=DogBreedGroup, blank=True, null=True)

    # the phone number that texted this image
    phone_number = models.IntegerField(blank=True, null=True)

    # the image of the animal
    # image = models.ImageField(blank=True, null=True)

    # the geopoint of the image
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # the result of google image processing
    # for now we'll just store the json dump
    google_image_result = models.TextField(default='') #JSONField(default=dict)

    # the url of the image in the twilio cloud
    image_url = models.CharField(max_length=2048, blank=True, null=True)

    # the conversation, stored as gField(models.CharField(max_length=4096), default=list)

    # another way to achieve this would be to create a record for every message we wend, and foreign key
    # all of them to the
    # location information


# class RescueCenter(models.Model):
#     pass
#     name = models.CharField()



class Shelter(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()



