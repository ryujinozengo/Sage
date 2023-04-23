import random # random choice selection
import urllib.request # for checking valid internet connection
from googlesearch import search as srch # for opening wikipedia 1st link
import azure.cognitiveservices.speech as speechsdk # for speech recognition of input voice
import PROJ_dic
import PROJ_News
import PROJ_Time
import PROJ_Date
import PROJ_Menu
import PROJ_Songs
import PROJ_Email
import PROJ_Movie
#import PROJ_Dominos
import PROJ_Weather
import PROJ_Hangman
import PROJ_tic_tac_toe
import PROJ_Google_Youtube
import PROJ_Text_to_speech
from difflib import get_close_matches
from modules import *
from widgets import *


#INPUT TEXT
def input_type():
    PROJ_Text_to_speech.speech("Type below what you want me to do")
    return input("Type below : \n")

#INPUT SPEECH
def input_speech():
    listener = speechsdk.SpeechConfig(subscription="8ef9bc73c3914aaa9cc945229520fb66", region="centralindia")
    listener.speech_recognition_language="en-IN"
    receiver = speechsdk.audio.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.SpeechRecognizer(speech_config=listener, audio_config=receiver)
    print("Listening")
    command = recognizer.recognize_once_async().get()

    if(command.reason == speechsdk.ResultReason.RecognizedSpeech):
        command = command.text
        command = command.strip()
        if(command[len(command)-1] == '.' or command[len(command)-1] == '?' or command[len(command)-1] == '!'):
            command = command[slice(len(command)-1)]
        print(command)
        return command.lower()
    else:
        print("Nothing Recognized")
        PROJ_Text_to_speech.speech("Nothing Recognnized Please try again")
        return -1

#search
def search(input_command,x):
    res = input_command.split()
    input_command = input_command.strip()
    c=0
    s=0
    for i in range(len(res)):

        if(res[i]=='play'):
            c=1
            break
        
        if(res[i]=='wikipedia'):
            c=2
            break
        
        if((i!=0 and res[i]=='in' and res[i-1]=='time')):
            c=3
            break
        if(i!=0 and res[i]=='time' and (res[i-1]=='present' or res[i-1]=='the')):    
            c=3
            if(res[i]=='time' and (i==len(res))):
                res.add('in')
            break
        if((i!=0 and res[i]=='now' and res[i-1]=='time')):
            c=3
            if(res[i]=='now' and (i==len(res))):
                res.add('in')
            elif(res[i]=='time' and (i==0)):
                res.add('in')
            break
        
        if(i+1!=len(res) and (res[i]=="today's" or res[i]=="current") and res[i+1]=='date'):
            c=4
            break

        if(input_command=="help me sending an email" or input_command=="send an email"):
            c=5
            break
        
        if(input_command=="suggest some movies"):
            c=6
            break
        
        if(input_command=="how is the weather today" or input_command=="today's weather" or input_command=='weather today'):
            c=7
            break
        
        if(input_command=="today's headlines" or input_command=="today's news" or input_command=="news"):
            c=8
            break
        
        if(input_command=="recommend some songs" or input_command=="trending songs" or input_command=="recommend songs"
            or input_command=="new songs" or input_command=="old songs"):
            c=9
            break
        
        if(input_command=="dictionary"):
            c=10
            break
        
        if(input_command=="game"):
            c=11
            break

        if(input_command=="order a pizza"):
            c=12
            break
        
    #Youtube
    if(c==1):
        PROJ_Text_to_speech.speech("Redirecting you to youtube")
        PROJ_Google_Youtube.youtube(input_command)
    
    #Wikipedia
    elif(c==2):
        print(input_command)
        for j in srch(input_command, tld="co.in", num=1, stop=1): 
            print(j)
            URL=j
        PROJ_Text_to_speech.speech("Redirecting you to wikipedia")
        PROJ_Google_Youtube.google(URL)
    
    #Time
    elif(c==3):
        PROJ_Time.time(res)
    
    #Date
    elif(c==4):
        PROJ_Date.date()
    
    #Email
    elif(c==5):
        PROJ_Email.email_sender(x)
    
    #Movies
    elif(c==6):
        PROJ_Menu.moviemnu()
        ch = input_speech()
        if(ch == "-1"):
            ch = input_speech()

        chs = ["top 250 movies of all time", "popular", "all time box office movies", "in theatres now", "coming soon"]
        x = get_close_matches(ch, chs)
        ch = x[0]
        
        if(ch=="1" or ch=="top 250 movies of all time"):
            PROJ_Movie.top250()
        elif(ch=="2" or ch=="popular"):
            PROJ_Movie.popular()
        elif(ch=="3" or ch=="all time box office movies"):
            PROJ_Movie.boxofficealltime()
        elif(ch=="4" or ch=="in theatres now"):
            PROJ_Movie.theaters()
        elif(ch=="5" or ch=="coming soon"):
            PROJ_Movie.comingsoon()
        else:
            print("Wrong choice")
    
    #Weather
    elif(c==7):
        PROJ_Weather.wea()
    
    #News
    elif(c==8):
        PROJ_News.news()
    
    #Music
    elif(c==9):
        if(input_command=="recommend some songs" or input_command=="recommend songs"):
            rand=random.choice([1,2,3])
            if(rand==1):
                PROJ_Songs.trending_song()
            elif(rand==2):
                PROJ_Songs.new_song()
            else:
                PROJ_Songs.old_song()
        elif(input_command=="trending songs"):
            PROJ_Songs.trending_song()
        elif(input_command=="new songs"):
            PROJ_Songs.new_song()
        elif(input_command=="old songs"):
            PROJ_Songs.old_song()
    
    #Dictionary
    elif(c==10):
        PROJ_dic.dict()
    
    #Game
    elif(c==11):
        r=random.choice([0,1])
        if(r==0):
            PROJ_Hangman.hm()
        else:
            PROJ_tic_tac_toe.ttt()
    
    #Dominos
    elif(c==12):
        PROJ_Dominos.pizza()

    #Google
    else:
        input_command=input_command.replace(' ','+')
        URL='http://google.com/search?q='+input_command
        PROJ_Text_to_speech.speech("Redirecting you to google")
        PROJ_Google_Youtube.google(URL)

#MAIN FUNCTION
def logic_main(self):
    PROJ_Menu.mnu(self)
    
    """

    try:
        while(True):
            print("Press t to search by typing or v for voice searching : ")
            x=input()
            print("------------")
            with urllib.request.urlopen("https://www.google.co.in") as response:
                input_command=-1
                if(x=='t'):
                    input_command=input_type()
                elif(x=='v'):
                    input_command=input_speech()
                else:
                    print("Wrong Input")
                if(input_command != -1):
                    if(input_command.lower()=="exit" or input_command.lower()=="stop"):
                        print("ADIOS AMIGO...POWERING OFF !")
                        PROJ_Text_to_speech.speech("Adios amigo")
                        PROJ_Text_to_speech.speech("Powering off")
                    else:
                        search(input_command.lower(),x)

    except:
        print("Can't provide any solution for that at the moment !")
        print("ADIOS AMIGO...POWERING OFF !")
        PROJ_Text_to_speech.speech("Can't provide any solution for that at the moment !")
    """
