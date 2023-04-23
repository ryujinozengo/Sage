import random # random choice selection
import urllib.request # for checking valid internet connection
from googlesearch import search as srch # for opening wikipedia 1st link
import azure.cognitiveservices.speech as speechsdk # for speech recognition of input voice


import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 190)

# Speech
def speech(text):
    engine.say(text)
    engine.runAndWait()

#INPUT TEXT
def input_type():
    # speech("Type below what you want me to do")
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 190)

    def speech(text):
        engine.say(text)
        engine.runAndWait()

    speech("Type below what you want me to do")

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
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 190)

        def speech(text):
            engine.say(text)
            engine.runAndWait()

        speech("Nothing Recognnized Please try again")
        # speech("Nothing Recognnized Please try again")
        return -1

#search
def search(input_command,x):
    res = input_command.split()
    input_command = input_command.strip()
    print(input_command)
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
        # speech("Redirecting you to youtube")
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 190)

        def speech(text):
            engine.say(text)
            engine.runAndWait()

        speech("Redirecting you to youtube")

        
        # PROJ_Google_Youtube.youtube(input_command)
        import webbrowser # for google search
        import pywhatkit # for youtube search

        #Search on youtube
        def youtube(ic):
            pywhatkit.playonyt(ic)
            print("Task executed")
        youtube(input_command)

        
    
    #Wikipedia
    elif(c==2):
        from googlesearch import search as srch
        import webbrowser
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 190)

        def speech(text):
            engine.say(text)
            engine.runAndWait()
        
        # tld="co.in"
        # num=1 
        # stop=1
        for j in srch(input_command, 1): 
            URL=j
        speech("Redirecting you to wikipedia")

        webbrowser.open_new_tab(URL)

    
    #Time
    elif(c==3):
        # PROJ_Time.time(res)
        import geocoder # get present location
        from geopy.geocoders import Nominatim # search for location
        from timezonefinder import TimezoneFinder # find time zone of ip
        import datetime # find date and time
        import pytz # date and time of any country
        
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 190)
        
        def speech(text):
            engine.say(text)
            engine.runAndWait()


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
            speech("The current time is "+time)
        time(res)



    #Date
    elif(c==4):
        # PROJ_Date.date()
        import geocoder # get present location
        from timezonefinder import TimezoneFinder # find time zone of ip
        import datetime # find date and time
        import pytz # date and time of any country
        
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 190)

        # Speech
        def speech(text):
            engine.say(text)
            engine.runAndWait()

        def date():
            location = geocoder.ip('me')
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.lng, lat=location.lat)
            current_time = datetime.datetime.now(pytz.timezone(result)) 
            date = current_time.strftime("%d/%m/%Y")
            print("Today's date is : ",date)
            date = current_time.strftime("%m/%d/%Y")
            speech("Today's date is")
            speech(date)

        date()

    #Email
    elif(c==5):
        # PROJ_Email.email_sender(x)
        import azure.cognitiveservices.speech as speechsdk # for speech recognition
        import smtplib # for email server
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders
        
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 190)

        # Speech
        def speech(text):
            engine.say(text)
            engine.runAndWait()

        def email_sender(x):
            try:
                def input_speech():
                    listener = speechsdk.SpeechConfig(subscription="8ef9bc73c3914aaa9cc945229520fb66", region="centralindia")
                    listener.speech_recognition_language="en-IN"
                    receiver = speechsdk.audio.AudioConfig(use_default_microphone=True)
                    recognizer = speechsdk.SpeechRecognizer(speech_config=listener, audio_config=receiver)
                    print("Listening")
                    command = recognizer.recognize_once_async().get()

                    if(command.reason == speechsdk.ResultReason.RecognizedSpeech):
                        command = command.text
                        print(command)
                        return command
                    else:
                        print("Nothing Recognized !! Please type in :")
                        speech("Nothing Recognnized Please type in")
                        return input()


                sender = "legtgsrk613@gmail.com"
                print("Type in the receiver email address : ")
                speech("Type in the receiver email address")
                receiver = input()

                msg = MIMEMultipart()
                msg['From'] = sender
                msg['To'] = receiver

                print("Enter subject : ")
                speech("Enter subject")
                if(x=='t'):
                    msg['Subject'] = input()
                else:
                    msg['Subject'] = input_speech()

                print("Enter body : ")
                speech("Enter body")
                if(x=='t'):
                    body = input()
                else:
                    body = input_speech()
                msg.attach(MIMEText(body, 'plain'))

                print("Enter file name : ")
                speech("Enter file name")
                filename = input()
                if(filename.lower() != "none"):
                    print("Enter path : ")
                    speech("Enter path")
                    att=input()
                    flag=0
                    for i in att:
                        if flag==1:
                            i="\\"
                            break
                        if i==":":
                            flag=1

                    attachment = open(att, "rb")
                    p = MIMEBase('application', 'octet-stream')
                    p.set_payload((attachment).read())
                    encoders.encode_base64(p)
                    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                    msg.attach(p)

                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender, "dsuvetbdkizptecm")
                text = msg.as_string()
                s.sendmail(sender, receiver, text)
                s.quit()
                print("Email sent!")
                speech("Email sent")

            except:
                print("------------------------------------------------------------------------")
                print("You are either not connected to internet or the receiver email address")
                print("could not be found or the file name/location may have some errors.")
                print("Please try again")
                print("------------------------------------------------------------------------")

        email_sender('x')
    
    #Movies
    elif(c==6):
        import requests
        from difflib import get_close_matches
        # PROJ_Menu.moviemnu()
        print("\nChoose from the given list of type of movies :\n")
        print("1. TOP 250 movies of all time")
        print("2. Popular")
        print("3. All time box office movies")
        print("4. In theatres now")
        print("5. Coming soon")
        print("\nEnter your choice")
        
        ch = input_speech()
        if(ch == "-1"):
            ch = input_speech()

        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 190)
        
        def speech(text):
            engine.say(text)
            engine.runAndWait()
            

        chs = ["top 250 movies of all time", "popular", "all time box office movies", "in theatres now", "coming soon"]
        x = get_close_matches(ch, chs)
        ch = x[0]
        
        if(ch=="1" or ch=="top 250 movies of all time"):
            speech("We are displaying the top 250 movies")
            url = "https://imdb-api.com/en/API/Top250Movies/k_jgspbg01"
            r=requests.get(url).json()

            print("\n\n\033[4mTOP 250 movies of all time :\033[0m\n")
            c=0
            for i in r['items']:
                title = i['fullTitle']
                c=c+1
                print(str(c)+'.',title)
                
        elif(ch=="2" or ch=="popular"):
            speech("Displaying some popular movies")
            url = "https://imdb-api.com/en/API/MostPopularMovies/k_jgspbg01"
            r=requests.get(url).json()

            c=0
            print("\n\n\033[4mPopular movies now :\033[0m\n")
            for i in r['items']:
                title = i['fullTitle']
                c=c+1
                print(str(c)+'.',title)

        elif(ch=="3" or ch=="all time box office movies"):
            speech("Displaying the all time box office movies")
            url = "https://imdb-api.com/en/API/BoxOfficeAllTime/k_jgspbg01"
            r=requests.get(url).json()

            c=0
            print("\n\n\033[4mAll time box office movies :\033[0m\n")
            for i in r['items']:
                title = i['title']
                c=c+1
                print(str(c)+'.',title)
        
        elif(ch=="4" or ch=="in theatres now"):
            speech("Displaying some movies which are in theatres now")
            url = "https://imdb-api.com/en/API/InTheaters/k_jgspbg01"
            r=requests.get(url).json()

            c=0
            print("\n\n\033[4mMovies in theatres now :\033[0m\n")
            for i in r['items']:
                title = i['fullTitle']
                c=c+1
                print(str(c)+'.',title)

        elif(ch=="5" or ch=="coming soon"):
            speech("Some coming soon movies are displayed below")
            url = "https://imdb-api.com/en/API/ComingSoon/k_jgspbg01"
            r=requests.get(url).json()

            c=0
            print("\n\n\033[4mMovies coming soon :\033[0m\n")
            for i in r['items']:
                title = i['fullTitle']
                c=c+1
                print(str(c)+'.',title)

        else:
            print("Wrong choice")
    
    #Weather
    elif(c==7):
        # PROJ_Weather.wea()
        import requests
        from bs4 import BeautifulSoup
        
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 190)
        
        def speech(text):
            engine.say(text)
            engine.runAndWait()

        def wea():
            print("Enter name of place (or just type 'here' if u want weather of your present location): ")
            speech("Enter name of place (or just type 'here' if u want weather of your present location)")
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

                    speech("In "+plce)
                    speech("the temperature is "+temp)
                    speech("and the weather is "+weathr)
                else:
                    print("Place :- "+plc)
                    print("Temperature :- "+temp)
                    print("Weather type :- "+weathr)

                    speech("In "+plc)
                    speech("the temperature is "+temp)
                    speech("and the weather is "+weathr)

            except:
                print("Sorry, can't find the place. Can you give name of a more generalised place!!")
                speech("Sorry, can't find the place") 
                speech("Can you give name of a more generalised place")
        wea()
    
    #News
    elif(c==8):
        # PROJ_News.news()
        import requests
        import pymsgbox
        from bs4 import BeautifulSoup
        import hyperlink
        from googlesearch import search as srch
        
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 190)
        
        def speech(text):
            engine.say(text)
            engine.runAndWait()



        def news():
            print()
            speech("Loading your feed")
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
            speech("Today's headlines")
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
                        #speech(news[i])
                        break
            """
            for i in range(len(news)):
                if(news[i] not in dlt):
                    print(str(i+1)+". "+news[i])
        news()
    
    #Music
    elif(c==9):
        import requests
        import random
        from bs4 import BeautifulSoup
        
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 190)
        
        def speech(text):
            engine.say(text)
            engine.runAndWait()


        def trending_song():
            print()
            print("\033[4mTrending songs\033[0m")
            speech("Showing you some trending songs")
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
            speech("Some newly released songs are waiting for you below")
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
            speech("Presenting to you those nostalgic old songs")
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

        if(input_command=="recommend some songs" or input_command=="recommend songs"):
            rand=random.choice([1,2,3])
            if(rand==1):
                trending_song()
            elif(rand==2):
                new_song()
            else:
                old_song()
        
        elif(input_command=="trending songs"):
            trending_song()
        
        elif(input_command=="new songs"):
            new_song()
        
        elif(input_command=="old songs"):
            old_song()
    
    #Dictionary
    elif(c==10):
        import json
        import time
        import speech_recognition as sr
        import azure.cognitiveservices.speech as speechsdk
        from difflib import get_close_matches
        
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 190)
        
        # Speech
        def speech(text):
            engine.say(text)
            engine.runAndWait()

        data = json.load(open("dicdata.json"))

        def check(x):
            if(x.lower() in data):
                print("SEARCH RESULTS FOUND-----------------------------------------------------------------------------")
                return data[x.lower()]
            elif(x.upper() in data):
                print("SEARCH RESULTS FOUND-----------------------------------------------------------------------------")
                return data[x.upper()]
            elif(x.title() in data):
                print("SEARCH RESULTS FOUND-----------------------------------------------------------------------------")
                return data[x.title()]
            else:
                print("SEARCH RESULTS FOUND-----------------------------------------------------------------------------")
                print("Word not found")
                speech("word not found")
                print("But we have got the closest match. Have a look at it")
                speech("But we have got the closest match. Have a look at it")
                m=get_close_matches(x , data.keys())[0]
                print("The word :- ", m)
                return data[m]
        
        def micro():
            listener = speechsdk.SpeechConfig(subscription="8ef9bc73c3914aaa9cc945229520fb66", region="centralindia")
            #listener = speechsdk.SpeechConfig(subscription="bad56e16463a403dad64f587c55e4d81", region="centralindia")
            listener.speech_recognition_language="en-IN"
            receiver = speechsdk.audio.AudioConfig(use_default_microphone=True)
            recognizer = speechsdk.SpeechRecognizer(speech_config=listener, audio_config=receiver)
            print("Listening(microsoft)...")
            command = recognizer.recognize_once_async().get()
            if(command.reason == speechsdk.ResultReason.RecognizedSpeech):
                command = command.text
                command = command.strip()
                if(command[len(command)-1] == '.'):
                    command = command[slice(len(command)-1)]
                print(command.lower())
                return command.lower()
            else:
                print("Nothing Recognized")
                return -1


        def dict():
            print("Enter the word you need to search : ")
            speech("Enter the word you need to search")
            x=micro()
            print("")
            ans=check(x)
            speech("Search Results found")
            c=1
            if(type(ans)==list):
                for i in ans:
                    print(str(c)+"." , i)
                    speech("Number"+str(c))
                    speech(i)
                    c+=1
                c=1
            else:
                print(ans)
            print("--------------------------------------------------------------------------------------------------")
            print("")

        dict()
        # PROJ_dic.dict()
    
    #Game
    elif(c==11):
        r=random.choice([0,1])
        if(r==0):
            #PROJ_Hangman.hm()
            import random
            import winsound
            import pyttsx3
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', 190)
        
            def speech(text):
                engine.say(text)
                engine.runAndWait()


            def hang(n,str):
                if(n==9):
                    print("9 turns left")
                    print("-------")
                elif(n==8):
                    print("8 turns left")
                    print("-------")
                    print("  O    ")
                elif(n==7):
                    print("7 turns left")
                    print("-------")
                    print("  O    ")
                    print("  |    ")
                elif(n==6):
                    print("6 turns left")
                    print("-------")
                    print("  O    ")
                    print("  |    ")
                    print(" /     ")
                elif(n==5):
                    print("5 turns left")
                    print("-------")
                    print("  O    ")
                    print("  |    ")
                    print(" / \   ")
                elif(n==4):
                    print("4 turns left")
                    print("-------")
                    print("\ O    ")
                    print("  |    ")
                    print(" / \   ")
                elif(n==3):
                    print("3 turns left")
                    print("-------")
                    print("\ O /  ")
                    print("  |    ")
                    print(" / \   ")
                elif(n==2):
                    print("2 turns left")
                    print("-------")
                    print("\ O /- ")
                    print("  |    ")
                    print(" / \   ")
                elif(n==1):
                    print("1 turn left")
                    print("-------")
                    print("\ O /_|")
                    print("  |   ")
                    print(" / \  ")
                elif(n==0):
                    print("You lose. You let the kind man hang to death.")
                    print("-----")
                    print(" O_|")
                    print("/|\  ")
                    print("/ \  ")
                    print("---------------------------------------------")
                    print("The word is",str)
                    print("------------------------------------")
                    speech("You lose")
                    speech("You could not save the innocent man from dying")
            def hm():
                print("------------------------------------")
                print("WELCOME TO HANGMAN GAME")
                print("Try to guess the word before I finish my drawing of Hanging the Man.")
                print("You have 10 attempts to guess the word correctly")
                speech("welcome to hangman")
                speech("You have 10 attempts to guess the word else the innocent man will be hanged to death")

                x=["hi","cat","home","country","computer","irc","hat","wow","Berlin","fly","airplane","cow","maps","make","run","sigh","golf","running","hat","television","games","hangman","pearl","cat","dog","snake","black","white","cabin","trees","birds","animals"]
                str=random.choice(x)
                length=len(str)
                word=[]
                new=[]
                j=1
                flag=0
                count=10
                l=0
                lastflag=0
                while(j<=length):
                    new.append("_ ")
                    word.append(str[j-1])
                    j+=1
                new.append(" ")
                while(True):
                    l=0
                    flag=0
                    lastflag=0
                    print("")
                    print("Guess the word :-", end=" ")
                    for i in new:
                        print(i, end="")

                    a=input()

                    for i in word:
                        if(i==a):
                            new[l]=a
                            flag+=1
                        l+=1
                    if(flag==0):
                        count-=1
                        hang(count,str)
                        winsound.Beep(440, 800)
                    if(flag!=0):
                        print("Right guess !")
                        speech("Right  guess")
                    for i in new:
                        if(i=="_ "):
                            lastflag+=1
                    if(lastflag==0):
                        print("CONGRATULATIONS!!!  YOU WIN !!!... You have guessed the word right.You saved the kind man from being hanged")
                        print("The word is",str)
                        print("------------------------------------")
                        speech("Congratulations")
                        speech("you saved the innocent man from dying")
                        break
                    if(count==0):
                        break  
            hm()
        else:
            # PROJ_tic_tac_toe.ttt()
            import random
            
            import pyttsx3
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', 190)

            def speech(text):
                engine.say(text)
                engine.runAndWait()


            board = [' ' for x in range(10)]
            board[0]='#'

            def insertLetter(letter,pos):
                board[pos]=letter

            def spaceIsFree(pos):
                return board[pos]==' '

            def isBoardFull(board):
                if(board.count(' ')==0):
                    return True
                else:
                    return False

            def printBoard(board):
                print()
                print("-------------------------")
                print('   |   |   ')
                print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
                print('   |   |   ')
                print('-----------')
                print('   |   |   ')
                print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
                print('   |   |   ')
                print('-----------')
                print('   |   |   ')
                print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
                print('   |   |   ')
                print("------------------------")
                print()

            def IsWinner(b,l):
                return ((b[1]==l and b[2]==l and b[3]==l) or (b[4]==l and b[5]==l and b[6]==l) or
                        (b[7]==l and b[8]==l and b[9]==l) or (b[1]==l and b[4]==l and b[7]==l) or
                        (b[2]==l and b[5]==l and b[8]==l) or (b[3]==l and b[6]==l and b[9]==l) or
                        (b[1]==l and b[5]==l and b[9]==l) or (b[3]==l and b[5]==l and b[7]==l))

            def playerMove():
                while True:
                    print("Please select a position to enter the X between 1 to 9 :- ")
                    speech("Please enter your move")
                    move = input()
                    print("-----------")

                    try:
                        move = int(move)
                        if (move > 0 and move < 10):
                            if spaceIsFree(move):
                                insertLetter('X' , move)
                                break
                            else:
                                print('Sorry, this space is occupied')
                                speech("The place is occupied")
                        else:
                            print('Please type a number between 1 and 9 :-')
                            speech("Type a number between 1 and 9")

                    except:
                        print('Please type a number')
                        speech("Please type a number")
                        playerMove()

            def computerMove():
                possibleMoves=[]
                for i in range(len(board)):
                    if(board[i]==' '):
                        possibleMoves.append(i)
                move=0

                for j in ['O','X']:
                    for i in possibleMoves:
                        boardcopy = board[:]
                        boardcopy[i]=j
                        if IsWinner(boardcopy,j):
                            move=i
                            return move

                if((board[1]=='X' and board[5]=='O' and board[9]=='X')or(board[3]=='X' and board[5]=='O' and board[7]=='X')):
                    edgesOpen=[]
                    for i in possibleMoves:
                        if i in [2,4,6,8]:
                            edgesOpen.append(i)
                    if len(edgesOpen)>0:
                        return random.choice(edgesOpen)
                    cornerOpen=[]
                    for i in possibleMoves:
                        if i in [1,3,7,9]:
                            cornerOpen.append(i)
                    if len(cornerOpen)>0:
                        return random.choice(cornerOpen)

                if 5 in possibleMoves:
                    move=5
                    return move

                cornerOpen=[]
                for i in possibleMoves:
                    if i in [1,3,7,9]:
                        cornerOpen.append(i)
                if len(cornerOpen)>0:
                    return random.choice(cornerOpen)

                edgesOpen=[]
                for i in possibleMoves:
                    if i in [2,4,6,8]:
                        edgesOpen.append(i)
                if len(edgesOpen)>0:
                    return random.choice(edgesOpen)

            def ttt():
                print()
                print("WELCOME TO TIC-TAC-TOE")
                print("------------------------------------------")
                speech("Welcome to tic tac toe")
                printBoard(board)
                while not(isBoardFull(board)):
                    if not(IsWinner(board,'O')):
                        playerMove()
                        printBoard(board)
                    else:
                        print("You lose!")
                        speech("You lose")
                        break
                    
                    if not(IsWinner(board,'X')):
                        move=computerMove()
                        if(move==None or move==0):
                            print("")
                        else:
                            insertLetter('O',move)
                            print("Computer placed O in position ",move)
                            printBoard(board)
                            speech("Computer made is move in position"+str(move))
                    else:
                        print("You win")
                        speech("Congratulations You win")
                        break
                    
                if isBoardFull(board):
                    print("Tie game")
                    speech("The matched ended in a draw")
            ttt()
    
    #Dominos
    elif(c==12):
        #PROJ_Dominos.pizza()
        import difflib
        import pyttsx3
        from time import sleep
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import azure.cognitiveservices.speech as speechsdk
        from selenium.webdriver.support.ui import WebDriverWait
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.support import expected_conditions as EC

        def speech(text):
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', 190)

            engine.say(text)
            engine.runAndWait()


        def inp():
            listener = speechsdk.SpeechConfig(subscription="8ef9bc73c3914aaa9cc945229520fb66", region="centralindia")
            listener.speech_recognition_language="en-IN"
            receiver = speechsdk.audio.AudioConfig(use_default_microphone=True)
            recognizer = speechsdk.SpeechRecognizer(speech_config=listener, audio_config=receiver)
            print("Listening")
            speech("Listening")
            command = recognizer.recognize_once_async().get()

            if(command.reason == speechsdk.ResultReason.RecognizedSpeech):
                command = command.text
                command = command.strip()
                if(command[len(command)-1] == '.'):
                    command = command[slice(len(command)-1)]
                print(command)
                return command.lower()
            else:
                print("Nothing Recognized")
                speech("Nothing Recognized Please try again")
                return "-1"


        def pizza():        
            #location = input('Enter your location : ')
            location = "123 Dr. Saroj Nath Mukherjee Street Uttarpara Hooghly"

            #email = input('Enter your email : ')
            email = "soham2001sen@gmail.com"

            #driver = webdriver.Chrome(r"Chromedriver.exe")
            #driver = webdriver.Chrome(r"C:\Users\soham\Desktop\Coding\Project\Voice Assistant\chromedriver.exe")
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()

            wait = WebDriverWait(driver, 30)
            wait2 = WebDriverWait(driver, 3)

            driver.get("https:\\www.dominos.co.in/")

            driver.find_element('link text','ORDER ONLINE NOW').click()
            sleep(2)

            try:
                wait2.until(EC.presence_of_element_located((By.XPATH, '//*[@id="desktopBannerWrapped"]/div/div[3]/div[1]/button[1]'))).click()
                sleep(2)
            except:
                """"""

            try:
                sleep(2)
                driver.switch_to.frame(0)
                wait2.until(EC.presence_of_element_located((By.XPATH, '//*[@id="close-icon"]'))).click()
                driver.switch_to.default_content()
                sleep(2)
            except:
                """"""

            try:
                wait2.until(EC.presence_of_element_located((By.XPATH, '//*[@id="desktopBannerWrapped"]/div/div[3]/div[1]/button[1]'))).click()
                sleep(2)
            except:
                """"""


            #location
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/input'))).click()
            sleep(2)

            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input'))).send_keys(location)
            sleep(2)

            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li'))).click()
            sleep(2)


            #login
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[2]'))).click()
            sleep(2)

            speech("Enter phone number")
            phn_no=inp()
            while(phn_no=="-1"):
                phn_no=inp()
            while(len(phn_no)!=10):
                speech("Wrong phone number please try again")
                phn_no=inp()

            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input'))).send_keys(phn_no)
            sleep(2)

            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input'))).click()
            sleep(2)

            speech("Enter otp")
            otp=inp()
            while(otp=="-1"):
                otp=inp()
            while(len(otp)!=6):
                speech("Wrong otp please try again")
                otp=inp()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input'))).send_keys(otp)
            sleep(2)

            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button'))).click()
            sleep(2)



            #MENU
            sleep(5)
            i = 0
            words = []
            all_items = driver.find_elements(By.XPATH, '//div[@class="itm-wrppr"]/div')

            for number, item in enumerate(all_items, 1):
            #for item in (all_items):
                name = item.get_attribute('data-label')
                words.append(name)
                print(words[i])
                i = i+1

            ss="ADD TO CART"
            dr=driver.find_elements(By.XPATH, "//span[contains(text(),'"+ss+"')]")
            addeditems = 0
            sleep(1)

            while(1<2):
                speech("Enter your order")
                s=inp()
                while(s=="-1"):
                    s=inp()

                res = s.split(',')

                for i in res:
                    i=i.strip()

                s = ' '.join(res)

                s=s.title()
                s=s.strip()
                print(s)
                x = difflib.get_close_matches(s, words)
                print(x)
                s = x[0]

                try:
                    c = 0
                    for i in words:
                        if(i==s):
                            dr[c].click()
                            addeditems += 1
                            break
                        else:
                            c+=1
                except:
                    print("Not found")

                try:
                    driver.find_element(By.XPATH, "//span[contains(text(),'"+"NO THANKS"+"')]")
                    speech("do you want to add extra cheese")
                    i=inp()
                    i=i.strip()
                    i=i.lower()
                    print(i)
                    while(i!="yes" and i!="no"):
                        speech("Wrong entry please try again")
                        i=inp()

                    if(i=="no"):
                        driver.find_element(By.XPATH, '//button[@class="btn--gry"]').click()
                    else:
                        driver.find_element(By.XPATH, '//button[@class="btn--grn"]').click()

                except:
                    """"""

                speech("Do you want to increase the number of this item ? please reply with yes or no ")
                ch = inp()
                while(ch == -1):
                    ch = inp()

                if(ch == "yes"):
                    speech("How many more items will you like to add ?")
                    cnt = int(inp())
                    for i in range(addeditems):
                        if(driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div['+str(i+1)+']/div/div/div[1]/div[2]/span[1]').text == s):
                            for j in range(cnt):
                                driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div['+str(i+1)+']/div/div/div[2]/div/div/div[2]/div').click()
                                sleep(1)
                else:
                    """"""


                speech("Do you want to add more items ?")
                ch = inp()
                while(ch == -1):
                    ch = inp()

                if(ch == "yes"):
                    continue
                else:
                    break
                
                
            #CHECKOUT
            speech("proceeding to checkout")
            sleep(1.5)
            driver.find_element(By.XPATH, "//span[contains(text(),'"+"CHECKOUT"+"')]").click()

            #ORDER PLACING
            speech("placing your order")
            sleep(1.5)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[7]/button'))).click()

            #ADDRESS and DETAILS
            speech("Enter your full name")
            name = inp()
            if(name == "-1"):
                speech("Nothing recognized try again")
                name = inp()
            res = name.split(" ")
            if(len(res)==1):
                first_name = res[0]
                last_name = " "
            else:
                last_name = res[len(res)-1]
                first_name = ""
                for n,i in enumerate(res,0):
                    first_name = first_name + i + " "
                    if(n == len(res)-2):
                        break
                    
            #first name
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[1]/div[1]/div/input')))
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[1]/div[1]/div/input').clear()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[1]/div[1]/div/input'))).send_keys(first_name)
            sleep(1)

            #last name
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[1]/div[2]/div/input')))
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[1]/div[2]/div/input').clear()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[1]/div[2]/div/input'))).send_keys(last_name)
            sleep(1)

            speech("Entering your mail address")
            email_address = email
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[2]/div/div/input')))
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[2]/div/div/input').clear()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[2]/div/div/input'))).send_keys(email_address)
            sleep(1)

            speech("Entering your address")
            address = location
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[3]/div[1]/div/input')))
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[3]/div[1]/div/input').clear()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[3]/div[1]/div/input'))).send_keys(address)
            sleep(1)

            speech("Enter your house number")
            house_no = inp()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[3]/div[2]/div/input')))
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[3]/div[2]/div/input').clear()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[3]/div[2]/div/input'))).send_keys(house_no)
            sleep(1)

            speech("saving and continue")
            sleep(1)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/input'))).click()
            sleep(2)


            #speech("confirming your order")
            #sleep(1)
            #wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/button'))).click()

            sleep(40)

        pizza()

    #Google
    else:
        input_command=input_command.replace(' ','+')
        URL='http://google.com/search?q='+input_command
        # speech("Redirecting you to google")
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 190)

        def speech(text):
            engine.say(text)
            engine.runAndWait()
        speech("Redirecting you to google")

        import webbrowser # for google search
        import pywhatkit # for youtube search

        #search on google
        def google(url):
            webbrowser.open_new_tab(url)
            print("Task executed")
        google(URL)



def mnu():
    print("---------------------------------------------------------------------------------------------------")
    print("The possible things you can tell to the virtual assistant")
    print("MENU :-")
    print("\nYoutube :- Play <something>                              Wikipedia :- Have the word 'wikipedia'")
    print("\nDate :- today's date / current date                      Dictionary :- only type 'dictionary' first")
    print("\nEmail :- Help me sending an email/send an email          Movies :- Suggest some movies")
    print("\nWeather :- How is the weather today/today's weather      Game :- the keyword 'game'")
    print("\nTime :- has the following keywords - time in <place>/    Songs :- recommend some songs/ recommend songs/")
    print("        present time/ the time/ time now                          trending songs/ new songs/ old songs")
    print("\nNews :- Today's headlines / today's news / news          Google :- Anything except these")
    print("\nWill you like to order a pizza ? - Just ask <Order a pizza>")
    print()
    print("--------------------------------------------------------------------------------------------------")


#MAIN FUNCTION
mnu()
# speech("Hi")
# speech("I am Bishhokosh")
# speech("The menu for the works I can do is given below")

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
                    speech("Adios amigo")
                    speech("Powering off")
                else:
                    search(input_command.lower(),x)

except:
    print("Can't provide any solution for that at the moment !")
    print("ADIOS AMIGO...POWERING OFF !")
    speech("Can't provide any solution for that at the moment !")
