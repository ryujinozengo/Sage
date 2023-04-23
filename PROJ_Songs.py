import requests
from bs4 import BeautifulSoup
import PROJ_Text_to_speech

def trending_song():
    print()
    print("\033[4mTrending songs\033[0m")
    PROJ_Text_to_speech.speech("Showing you some trending songs")
    url="https://gaana.com/songs"
    res=requests.get(url)

    soup=BeautifulSoup(res.text, 'html.parser')
    headlines=soup.find_all('a',attrs={'class':"_tra t_over _plyCr"})
    print()

    i=0
    for x in headlines:
        print(x.text.strip(),end=" :- ")
        print("https://gaana.com"+x['href'])
        print()

def new_song():
    print()
    print("\033[4mNew Release songs\033[0m")
    PROJ_Text_to_speech.speech("Some newly released songs are waiting for you below")
    url="https://gaana.com/newrelease/hindi"
    res=requests.get(url)

    soup=BeautifulSoup(res.text, 'html.parser')
    headlines=soup.find_all('a',attrs={'class':"al t_over"})
    print()

    i=0
    for x in headlines:
        print(x.text.strip(),end=" :- ")
        print("https://gaana.com"+x['href'])
        print()


def old_song():
    print()
    print("\033[4mOld songs\033[0m")
    PROJ_Text_to_speech.speech("Presenting to you those nostalgic old songs")
    #url="https://gaana.com/old-songs/hindi"
    url="https://gaana.com/playlist/gaana-dj-retro-top-50"
    res=requests.get(url)

    soup=BeautifulSoup(res.text, 'html.parser')
    headlines=soup.find_all(class_="_tra t_over _plyCr")
    print()

    i=0
    for x in headlines:
        print(x.text.strip(),end=" :- ")
        print("https://gaana.com"+x['href'])
        print()


#trending_song()
#new_song()
#old_song()