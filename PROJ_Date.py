import geocoder # get present location
from timezonefinder import TimezoneFinder # find time zone of ip
import datetime # find date and time
import pytz # date and time of any country
import PROJ_Text_to_speech

def date():
    location = geocoder.ip('me')
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.lng, lat=location.lat)
    current_time = datetime.datetime.now(pytz.timezone(result)) 
    date = current_time.strftime("%d/%m/%Y")
    print("Today's date is : ",date)
    date = current_time.strftime("%m/%d/%Y")
    PROJ_Text_to_speech.speech("Today's date is")
    PROJ_Text_to_speech.speech(date)

#date()