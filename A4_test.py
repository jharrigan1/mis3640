import json
import urllib.request
from pprint import pprint

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    return json.loads(response_text) 

def list_latLong(jresponse):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.    
    """
    whereabouts = []
    lat = jresponse['results'][0]['geometry']['location']['lat']
    lon = jresponse['results'][0]['geometry']['location']['lng']
    whereabouts.append(lat)
    whereabouts.append(lon)
    return whereabouts
 
def apiURL(placeoraddress):
    """
    Takes the name of a place or a given address and returns the API geocode request url for it 
    """
    addToLink = placeoraddress.replace(' ', '+')
    return 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyCf8_TxB2ELtA2kgDQZoVmZJHZZaufoK5w' %(addToLink)
 
def stops(loc):
    """
    Uses the coordinates from the user's address and returns the response from the mbta api
    """
    response_from_google = get_json(apiURL(loc))
    position = list_latLong(response_from_google)
    answerMBTA = get_json(urlMBTAapi(position))
    return answerMBTA
 
def urlMBTAapi(whereabouts):
    """Returns a MBTA API request url from a set of coordinates"""
    return 'http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=vSPU1c7EtEiU-JKg1C5dWA&lat=%s&lon=%s&format=json' %(whereabouts[0], whereabouts[1])

def alert_user(userLoc):
    """
    Takes the user location and prints the nearest station. If there is an index error,
    we told the function to alert the user that there is no nearby station. 
    """
    try:
        answerMBTA = stops(userLoc)
        name_of_stop = answerMBTA['stop'][0]['stop_name']
        totalDistance = float(answerMBTA['stop'][0]['distance'])
        print('The nearest MBTA station is located at %s, approximately %.2f miles from %s.' %(name_of_stop, totalDistance, userLoc))
    except IndexError:
        print('%s does not have a nearby MBTA station' %(userLoc))
 
def main():
    alert_user('Massachusetts Institute of Technology')
 
if __name__ == '__main__':
    main()