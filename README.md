# A 911 system for lost animals, enabling people to quickly send images or descriptions to a hotline that would map the report on a site for owners to find their pets.

Best Hack to Save Homeless Pets, HackHarvard 2017
![img_5056](https://user-images.githubusercontent.com/7296193/31972806-7e8cf2f6-b8f0-11e7-901b-a09dbf81d54b.jpg)


## Inspiration
- Losing a pet is terrifying.
- There is no standard method for handling lost and found animals.
- The problem of homeless pets evades technological solutions in part due to a lack of structured data.

## What it does
- Emergency hotline that anyone can contact to report an animal that they've lost or found.
- Chatbot asks for images and location data, and then connects the user.
- Images are analyzed, timestamped, geotagged and added to a comprehensive database of missing animals around the country.
- User is connected to closest animal rescue center.

## How we built it
- Twilio API sends and receives text, images, locations, and contact information for shelters.
- DialogFlow parses text messages and intelligently responds to users.
- Google Cloud Vision extracts features from images to help identify and categorize animals.
- PosgreSQL database using the PostGIS extension for geographic data stores the information.
- REST API atop a Django-python server hosted by Google Cloud exposes the database to queries.

## Challenges we ran into
- Most images captured by modern smart phone cameras contains location data. Our original plan was to extract geotags from a single image that we asked users to take of the animal. We didn't know that when images are sent over SMS, they are stripped of their metadata. Instead, we asked users to submit their location directly, which puts more burden on them but was ultimately more elegant from an engineering standpoint and guarantees more complete data.


## Accomplishments that we're proud of
- As a team that largely didn't know each other at the start of the hackathon, we're proud that we were able to come together, set a goal of what we wanted to accomplish over the course of the weekend, and succeed in doing so.
- We are proud of the elegance we see in our easy-to-use solution to a complex and important problem, and grateful to have the opportunity to work on it.

## What we learned
Members of our team used several technologies for the first time, including:
- Twilio
- PostgreSQL
- Webhooks
- REST
- Google Cloud
- AWS
- DialogFlow
- Python


## What's next for The Petrol
- We fundamentally believe that The Petrol is something that should exist. To become a 911-style service, The Petrol needs all the help it can get.
- As the database grows, The Petrol will begin to provide quantitative insights into the underlying causes of the homeless pet problem by using machine learning and tracking data over time to better understand, for example, what areas of cities should be targeted by TNR campaigns.
- There is potential to expand to help all animals without homes, building a database of pets up for adoption.
