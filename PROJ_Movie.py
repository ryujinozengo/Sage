import requests
import PROJ_Text_to_speech

def top250(): 
    PROJ_Text_to_speech.speech("We are displaying the top 250 movies")
    url = "https://imdb-api.com/en/API/Top250Movies/k_jgspbg01"
    r=requests.get(url).json()

    print("\n\n\033[4mTOP 250 movies of all time :\033[0m\n")
    c=0
    for i in r['items']:
        title = i['fullTitle']
        c=c+1
        print(str(c)+'.',title)

def popular():
    PROJ_Text_to_speech.speech("Displaying some popular movies")
    url = "https://imdb-api.com/en/API/MostPopularMovies/k_jgspbg01"
    r=requests.get(url).json()

    c=0
    print("\n\n\033[4mPopular movies now :\033[0m\n")
    for i in r['items']:
        title = i['fullTitle']
        c=c+1
        print(str(c)+'.',title)

def comingsoon():
    PROJ_Text_to_speech.speech("Some coming soon movies are displayed below")
    url = "https://imdb-api.com/en/API/ComingSoon/k_jgspbg01"
    r=requests.get(url).json()

    c=0
    print("\n\n\033[4mMovies coming soon :\033[0m\n")
    for i in r['items']:
        title = i['fullTitle']
        c=c+1
        print(str(c)+'.',title)

def boxofficealltime():
    PROJ_Text_to_speech.speech("Displaying the all time box office movies")
    url = "https://imdb-api.com/en/API/BoxOfficeAllTime/k_jgspbg01"
    r=requests.get(url).json()

    c=0
    print("\n\n\033[4mAll time box office movies :\033[0m\n")
    for i in r['items']:
        title = i['title']
        c=c+1
        print(str(c)+'.',title)

def theaters():
    PROJ_Text_to_speech.speech("Displaying some movies which are in theatres now")
    url = "https://imdb-api.com/en/API/InTheaters/k_jgspbg01"
    r=requests.get(url).json()

    c=0
    print("\n\n\033[4mMovies in theatres now :\033[0m\n")
    for i in r['items']:
        title = i['fullTitle']
        c=c+1
        print(str(c)+'.',title)


#top250()
#popular()
#boxofficealltime()
#comingsoon()
#theaters()