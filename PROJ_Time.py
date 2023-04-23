import geocoder # get present location
from geopy.geocoders import Nominatim # search for location
from timezonefinder import TimezoneFinder # find time zone of ip
import datetime # find date and time
import pytz # date and time of any country
import PROJ_Text_to_speech

def time(res):
    i=0
    for x in range(len(res)):
        if(res[x]=='in'):
            i=x
            break
    #for any location given
    if(res[i]=='in' and i!=len(res)):
        geolocator = Nominatim(user_agent="geoapiExercises")
        loc = res[i+1]
        location = geolocator.geocode(loc)
        if(location == None):
            print("No location of that name found")
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
    #for current location
    else:
        location = geocoder.ip('me')
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.lng, lat=location.lat)
    
    current_time = datetime.datetime.now(pytz.timezone(result)) 
    time = current_time.strftime("%H:%M")
    print("The current time is : ",time)
    PROJ_Text_to_speech.speech("The current time is "+time)

#time(["time","now","in","kolkata"])
#time(["time","now","in","canada"])