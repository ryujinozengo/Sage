import requests
import pymsgbox
from bs4 import BeautifulSoup
import hyperlink
from googlesearch import search as srch
import PROJ_Text_to_speech


def news():
    print()
    PROJ_Text_to_speech.speech("Loading your feed")
    print("'Bad news travel at the speed of light; good news travel like molasses.' - Tracy Morgan")
    print("Please wait while we try to bring you some good news.")
    print("Loading your feed...")
    print()

    url='https://www.bbc.com/news'
    response=requests.get(url)

    soup=BeautifulSoup(response.text, 'html.parser')
    headlines=soup.find('body').find_all('h3')
    dlt=["BBC World News TV", "BBC World Service Radio", "News daily newsletter", "Mobile app", "Get in touch"]
    news=[]
    News=[]
    for x in headlines:
        News.append(x.text.strip())

    for i in range(len(News)):
        if(News[i] not in dlt):
            if(News[i] not in news):
                news.append(News[i])

    news=news[0:10]

    URL=[]
    print("\033[4mTODAY'S TOP 10 HEADLINES\033[0m")
    PROJ_Text_to_speech.speech("Today's headlines")
    print()

    """
    for i in range(len(news)):
        if(news[i] not in dlt):
            for j in srch(news[i], tld="co.in", num=1, stop=1):
                url = hyperlink.parse(j)
                URL.append(url)
                #print(news[i],end=" :- ")
                #print(URL[i],end="\n\n")
                #pymsgbox.alert('TOP 10 HEADLINES', news[i])
                #PROJ_Text_to_speech.speech(news[i])
                break
    """
    for i in range(len(news)):
        if(news[i] not in dlt):
            print(str(i+1)+". "+news[i])
#news()