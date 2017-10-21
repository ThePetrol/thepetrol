'''
Created on Oct 21, 2017

@author: aditya sridhar
'''
"""
Locates the nearest shelter by:
    1) Determining the location of the user with latitude-longitude coordinates
    2) Querying "Animal rescue shelter" in search results
    3) Using Google Places API to search for the list of shelters near the location within a specified radius
    4) Choosing the closest location
"""

from google_places import GooglePlaces
from app import lang, ranking

DEBUG = True;

def locate(latitude, longitude):
    if(DEBUG):
        return '(505) 328-0879';    # Will's phone number
    
    # Create the dictionary for latitude and longitude
    lat_lng = {};
    lat_lng['lat'] = latitude;
    lat_lng['lng'] = longitude;
    
    # Create the query
    query = 'Animal rescue shelter';
    
    # Query for closest shelter
    google = GooglePlaces(api_key='AIzaSyD8GcHMHhfKLIa-gF9azq4sHwCeqNdE4Wc');
    result = google.nearby_search(lat_lng=lat_lng, name=query, rankby=ranking.DISTANCE);
    
    # Get nearest animal shelter with available phone number
    location_of_first_available_phone_number = -1;
    curr_location = 0;
    for shelter in result.places:
        shelter.get_details()
        if(not(shelter.local_phone_number is None)):
            location_of_first_available_phone_number = curr_location;
            break;
        curr_location += 1;

    # Return phone number of that shelter, if it exists
    if(curr_location == -1):
        return;
    nearest_shelter = result.places[location_of_first_available_phone_number];
    return nearest_shelter.local_phone_number;