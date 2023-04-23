import requests
from bs4 import BeautifulSoup
import PROJ_Text_to_speech

def wea():
    print("Enter name of place (or just type 'here' if u want weather of your present location): ")
    PROJ_Text_to_speech.speech("Enter name of place (or just type 'here' if u want weather of your present location)")
    plc=input()
    url="https://www.google.com/search?q=weather"
    if(plc.lower()=="here"):
        res=requests.get(url)
    else:
        res=requests.get(url+"+in+"+plc)
    
    soup=BeautifulSoup(res.text,'html.parser')
    try:
        temp=soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        weathr=soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        plce=soup.find('span', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        weathr=weathr.split('\n')[1]

        if(plc.lower()=="here"):
            print("Place :- "+plce)
            print("Temperature :- "+temp)
            print("Weather type :- "+weathr)

            PROJ_Text_to_speech.speech("In "+plce)
            PROJ_Text_to_speech.speech("the temperature is "+temp)
            PROJ_Text_to_speech.speech("and the weather is "+weathr)
        else:
            print("Place :- "+plc)
            print("Temperature :- "+temp)
            print("Weather type :- "+weathr)

            PROJ_Text_to_speech.speech("In "+plc)
            PROJ_Text_to_speech.speech("the temperature is "+temp)
            PROJ_Text_to_speech.speech("and the weather is "+weathr)

    except:
        print("Sorry, can't find the place. Can you give name of a more generalised place!!")
        PROJ_Text_to_speech.speech("Sorry, can't find the place") 
        PROJ_Text_to_speech.speech("Can you give name of a more generalised place")


#wea()