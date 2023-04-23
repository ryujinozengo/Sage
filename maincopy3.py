# ///////////////////////////////////////////////////////////////
#
# BY: GOGAN TRIBIKRAM GANGULY
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from FINAL_PROJ_main import *
#from final_main import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "GSS"
        description = "GSS"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_profile.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.mic_btn.clicked.connect(self.buttonClick)
        widgets.input_btn.clicked.connect(self.buttonClick)
        widgets.input_btn.clicked.connect(self.stop_loop)


        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////







        
        


        

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def cout_u(self,text):
        text = str(text)
        widgets.output.setTextColor(QColor(129, 141, 60, 255))
        widgets.output.setFontPointSize(14)
        if self.rebound == "Sage :":
            widgets.output.setFontWeight(700)
            widgets.output.append("User :")
            self.rebound = "User :"
        widgets.output.setFontWeight(500)
        widgets.output.append(text + "\n")
    

    def cout_c(self,text):
        text = str(text)
        widgets.output.setTextColor(QColor(120, 75, 48, 255))
        widgets.output.setFontPointSize(14)
        if self.rebound == "User :":
            widgets.output.setFontWeight(700)
            widgets.output.append("Sage :")
            self.rebound = "Sage :"

        widgets.output.setFontWeight(500)
        widgets.output.append(text + "\n")

    rebound ="User :"
    
    def cin(self):
        a=0
        self.clicked = False 
        while not self.clicked:
            #a = a + 1
            #print (a)
            QApplication.processEvents()
        text = ""
        text = widgets.input.text()
        if (len(text) == 0 ):
            self.clicked = False
            self.cout_c("No Input Provided") 
            return "No Input Provided"
        else:
            self.clicked = False
            self.cout_u(text)
            return text

        
        
       
    
    


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def stop_loop(self):
        self.clicked = True # Set a flag to indicate that the button has been clicked

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            

        # SHOW NEW PAGE
        if btnName == "btn_profile":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            text = " "
            self.cout_c(text)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

     


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("icon.ico"))
window = MainWindow()
app.processEvents()


































































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

    return window.cin()

#INPUT SPEECH
def input_speech():
        listener = speechsdk.SpeechConfig(subscription="8ef9bc73c3914aaa9cc945229520fb66", region="centralindia")
        listener.speech_recognition_language="en-IN"
        receiver = speechsdk.audio.AudioConfig(use_default_microphone=True)
        recognizer = speechsdk.SpeechRecognizer(speech_config=listener, audio_config=receiver)
        window.cout_c("Listening")
        speech("Listening")
        command = recognizer.recognize_once_async().get()

        if(command.reason == speechsdk.ResultReason.RecognizedSpeech):
            command = command.text
            command = command.strip()
            if(command[len(command)-1] == '.'):
                command = command[slice(len(command)-1)]
            window.cout_c(command)
            return command.lower()
        else:
            window.cout_c("Nothing Recognized")
            speech("Nothing Recognized Please try again")
            return "-1"

#search
def search(input_command,x):
    res = input_command.split()
    input_command = input_command.strip()
    a = str(input_command)
    window.cout_c(input_command)
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
        app.processEvents()
        
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
            window.cout_c("Task executed")
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
        
            
        for j in srch(input_command, 1): 
            URL=j
            app.processEvents()
        speech("Redirecting you to wikipedia")
        

        webbrowser.open_new_tab(URL)

    
    #Time
    elif(c==3):
        # import PROJ_Time
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
                app.processEvents()
            #for any location given
            if(res[i]=='in' and i!=len(res)):
                geolocator = Nominatim(user_agent="geoapiExercises")
                loc = res[i+1]
                location = geolocator.geocode(loc)
                if(location == None):
                    window.cout_c("No location of that name found")
                obj = TimezoneFinder()
                result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

            #for current location
            else:
                location = geocoder.ip('me')
                obj = TimezoneFinder()
                result = obj.timezone_at(lng=location.lng, lat=location.lat)

            current_time = datetime.datetime.now(pytz.timezone(result)) 
            time = current_time.strftime("%H:%M")
            window.cout_c("The current time is : " + time)
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
            window.cout_c("Today's date is : "+date)
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
                def input_speech_email():
                    listener = speechsdk.SpeechConfig(subscription="8ef9bc73c3914aaa9cc945229520fb66", region="centralindia")
                    listener.speech_recognition_language="en-IN"
                    receiver = speechsdk.audio.AudioConfig(use_default_microphone=True)
                    recognizer = speechsdk.SpeechRecognizer(speech_config=listener, audio_config=receiver)
                    window.cout_c("Listening")
                    command = recognizer.recognize_once_async().get()

                    if(command.reason == speechsdk.ResultReason.RecognizedSpeech):
                        command = command.text
                        window.cout_c(command)
                        return command
                    else:
                        window.cout_c("Nothing Recognized !! Please type in :")
                        speech("Nothing Recognnized Please type in")
                        return window.cin()


                sender = "legtgsrk613@gmail.com"
                window.cout_c("Type in the receiver email address : ")
                speech("Type in the receiver email address")
                receiver = window.cin()

                msg = MIMEMultipart()
                msg['From'] = sender
                msg['To'] = receiver

                window.cout_c("Enter subject : ")
                speech("Enter subject")
                if(x=='t'):
                    msg['Subject'] = window.cin()
                    app.processEvents()
                else:
                    msg['Subject'] = input_speech_email()

                window.cout_c("Enter body : ")
                speech("Enter body")
                if(x=='t'):
                    body = window.cin()
                else:
                    body = input_speech_email()
                msg.attach(MIMEText(body, 'plain'))

                window.cout_c("Enter file name : ")
                speech("Enter file name")
                app.processEvents()
                filename = window.cin()
                app.processEvents()
                if(filename.lower() != "none"):
                    window.cout_c("Enter path : ")
                    speech("Enter path")
                    att=window.cin()
                    app.processEvents()
                    flag=0
                    for i in att:
                        if flag==1:
                            i="\\"
                            break
                        if i==":":
                            flag=1
                        app.processEvents()

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
                window.cout_c("Email sent!")
                speech("Email sent")

            except:
                window.cout_c("------------------------------------------------------------------------")
                window.cout_c("You are either not connected to internet or the receiver email address")
                window.cout_c("could not be found or the file name/location may have some errors.")
                window.cout_c("Please try again")
                window.cout_c("------------------------------------------------------------------------")

        email_sender('t')
    
    #Movies
    elif(c==6):
        app.processEvents()
        import requests
        from difflib import get_close_matches
        # PROJ_Menu.moviemnu()
        window.cout_c("\nChoose from the given list of type of movies :\n")
        window.cout_c("1. TOP 250 movies of all time")
        window.cout_c("2. Popular")
        window.cout_c("3. All time box office movies")
        window.cout_c("4. In theatres now")
        window.cout_c("5. Coming soon")
        window.cout_c("\nEnter your choice")
        
        ch = input_speech()
        # if(ch == "-1"):
        #     ch = input_speech()

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

            window.cout_c("\n\n\033[4mTOP 250 movies of all time :\033[0m\n")
            c=0
            for i in r['items']:
                title = i['fullTitle']
                c=c+1
                window.cout_c(str(c) + '. ' + title)
                app.processEvents()
            app.processEvents()
                
        elif(ch=="2" or ch=="popular"):
            speech("Displaying some popular movies")
            url = "https://imdb-api.com/en/API/MostPopularMovies/k_jgspbg01"
            r=requests.get(url).json()

            c=0
            window.cout_c("\n\n\033[4mPopular movies now :\033[0m\n")
            for i in r['items']:
                title = i['fullTitle']
                c=c+1
                window.cout_c(str(c)+'. '+title)
                app.processEvents()
            app.processEvents()

        elif(ch=="3" or ch=="all time box office movies"):
            speech("Displaying the all time box office movies")
            url = "https://imdb-api.com/en/API/BoxOfficeAllTime/k_jgspbg01"
            r=requests.get(url).json()

            c=0
            window.cout_c("\n\n\033[4mAll time box office movies :\033[0m\n")
            for i in r['items']:
                title = i['title']
                c=c+1
                window.cout_c(str(c)+'. ' + title)
                app.processEvents()
            app.processEvents()
        
        elif(ch=="4" or ch=="in theatres now"):
            speech("Displaying some movies which are in theatres now")
            url = "https://imdb-api.com/en/API/InTheaters/k_jgspbg01"
            r=requests.get(url).json()

            c=0
            window.cout_c("\n\n\033[4mMovies in theatres now :\033[0m\n")
            for i in r['items']:
                title = i['fullTitle']
                c=c+1
                window.cout_c(str(c)+'. ' + title)
                app.processEvents()
            app.processEvents()

        elif(ch=="5" or ch=="coming soon"):
            speech("Some coming soon movies are displayed below")
            url = "https://imdb-api.com/en/API/ComingSoon/k_jgspbg01"
            r=requests.get(url).json()

            c=0
            window.cout_c("\n\n\033[4mMovies coming soon :\033[0m\n")
            for i in r['items']:
                title = i['fullTitle']
                c=c+1
                window.cout_c(str(c)+'. ' + title)
                app.processEvents()
            app.processEvents()

        else:
            window.cout_c("Wrong choice")
            app.processEvents()
    
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
            window.cout_c("Enter name of place (or just type 'here' if u want weather of your present location): ")
            speech("Enter name of place (or just type 'here' if u want weather of your present location)")
            plc=window.cin()
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
                    window.cout_c("Place :- "+plce)
                    window.cout_c("Temperature :- "+temp)
                    window.cout_c("Weather type :- "+weathr)

                    speech("In "+plce)
                    speech("the temperature is "+temp)
                    speech("and the weather is "+weathr)
                else:
                    window.cout_c("Place :- "+plc)
                    window.cout_c("Temperature :- "+temp)
                    window.cout_c("Weather type :- "+weathr)

                    speech("In "+plc)
                    speech("the temperature is "+temp)
                    speech("and the weather is "+weathr)

            except:
                window.cout_c("Sorry, can't find the place. Can you give name of a more generalised place!!")
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
            window.cout_c("\n")
            speech("Loading your feed")
            window.cout_c("'Bad news travel at the speed of light; good news travel like molasses.' - Tracy Morgan")
            window.cout_c("Please wait while we try to bring you some good news.")
            window.cout_c("Loading your feed...")
            window.cout_c("\n")

            url='https://www.bbc.com/news'
            response=requests.get(url)

            soup=BeautifulSoup(response.text, 'html.parser')
            headlines=soup.find('body').find_all('h3')
            dlt=["BBC World News TV", "BBC World Service Radio", "News daily newsletter", "Mobile app", "Get in touch"]
            news=[]
            News=[]
            for x in headlines:
                News.append(x.text.strip())
                app.processEvents()

            for i in range(len(News)):
                if(News[i] not in dlt):
                    if(News[i] not in news):
                        news.append(News[i])
                app.processEvents()

            news=news[0:10]

            URL=[]
            window.cout_c("\033[4mTODAY'S TOP 10 HEADLINES\033[0m")
            speech("Today's headlines")
            window.cout_c("\n")

            """
            for i in range(len(news)):
                if(news[i] not in dlt):
                    for j in srch(news[i], tld="co.in", num=1, stop=1):
                        url = hyperlink.parse(j)
                            URL.append(url)
                        #window.cout_c(news[i],end=" :- ")
                        #window.cout_c(URL[i],end="\n\n")
                        #pymsgbox.alert('TOP 10 HEADLINES', news[i])
                        #speech(news[i])
                        break
            """
            for i in range(len(news)):
                if(news[i] not in dlt):
                    window.cout_c(str(i+1)+". "+news[i])
                app.processEvents()
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
            window.cout_c("\n")
            window.cout_c("\033[4mTrending songs\033[0m")
            speech("Showing you some trending songs")
            url="https://gaana.com/songs"
            res=requests.get(url)

            soup=BeautifulSoup(res.text, 'html.parser')
            headlines=soup.find_all('a',attrs={'class':"_tra t_over _plyCr"})
            window.cout_c("\n")

            i=0
            a =""
            for x in headlines:
                a = str(x.text.strip()+ " :- ")
                window.cout_c(a)
                print(a)
                a = str("https://gaana.com"+x['href'])
                window.cout_c(a)
                print(a)
                window.cout_c("\n")
                app.processEvents()

        def new_song():
            window.cout_c("\n")
            window.cout_c("\033[4mNew Release songs\033[0m")
            speech("Some newly released songs are waiting for you below")
            url="https://gaana.com/newrelease/hindi"
            res=requests.get(url)

            soup=BeautifulSoup(res.text, 'html.parser')
            headlines=soup.find_all('a',attrs={'class':"al t_over"})
            window.cout_c("\n")

            i=0
            a =""
            for x in headlines:
                a = str(x.text.strip()+ " :- ")
                window.cout_c(a)
                print(a)
                a = str("https://gaana.com"+x['href'])
                window.cout_c(a)
                print(a)
                window.cout_c("\n")
                app.processEvents()


        def old_song():
            window.cout_c("\n")
            window.cout_c("\033[4mOld songs\033[0m")
            speech("Presenting to you those nostalgic old songs")
            #url="https://gaana.com/old-songs/hindi"
            url="https://gaana.com/playlist/gaana-dj-retro-top-50"
            res=requests.get(url)

            soup=BeautifulSoup(res.text, 'html.parser')
            headlines=soup.find_all(class_="_tra t_over _plyCr")
            window.cout_c("\n")

            i=0
            a=""
            for x in headlines:
                a = str(x.text.strip()+ " :- ")
                window.cout_c(a)
                print(a)
                a = str("https://gaana.com"+x['href'])
                window.cout_c(a)
                print(a)
                window.cout_c("\n")
                app.processEvents()

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
                window.cout_c("SEARCH RESULTS FOUND-----------------------------------------------------------------------------")
                return data[x.lower()]
            elif(x.upper() in data):
                window.cout_c("SEARCH RESULTS FOUND-----------------------------------------------------------------------------")
                return data[x.upper()]
            elif(x.title() in data):
                window.cout_c("SEARCH RESULTS FOUND-----------------------------------------------------------------------------")
                return data[x.title()]
            else:
                window.cout_c("SEARCH RESULTS FOUND-----------------------------------------------------------------------------")
                window.cout_c("Word not found")
                speech("word not found")
                window.cout_c("But we have got the closest match. Have a look at it")
                speech("But we have got the closest match. Have a look at it")
                m=get_close_matches(x , data.keys())[0]
                window.cout_c("The word :- " + m)
                return data[m]
        
        def micro():
            listener = speechsdk.SpeechConfig(subscription="8ef9bc73c3914aaa9cc945229520fb66", region="centralindia")
            listener.speech_recognition_language="en-IN"
            receiver = speechsdk.audio.AudioConfig(use_default_microphone=True)
            recognizer = speechsdk.SpeechRecognizer(speech_config=listener, audio_config=receiver)
            speech("Listening")
            command = recognizer.recognize_once_async().get()

            if(command.reason == speechsdk.ResultReason.RecognizedSpeech):
                command = command.text
                command = command.strip()
                if(command[len(command)-1] == '.'):
                    command = command[slice(len(command)-1)]
                return command.lower()
            else:
                speech("Nothing Recognized Please try again")
                return "-1"


        def dict():
            window.cout_c("Enter the word you need to search : ")
            speech("Enter the word you need to search")
            x=micro()
            window.cout_c("")
            ans=check(x)
            speech("Search Results found")
            c=1
            if(type(ans)==list):
                for i in ans:
                    window.cout_c(str(c)+"." + i)
                    speech("Number"+str(c))
                    speech(i)
                    c+=1
                    app.processEvents()
                c=1
            else:
                window.cout_c(ans)
            window.cout_c("--------------------------------------------------------------------------------------------------")
            window.cout_c("")

        dict()
        # PROJ_dic.dict()
    
    #Game
    elif(c==11):
        import random
        #r=random.choice([0,1])
        r=0
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
                    window.cout_c("9 turns left")
                    window.cout_c("-------")
                elif(n==8):
                    window.cout_c("8 turns left")
                    window.cout_c("-------")
                    window.cout_c("  O    ")
                elif(n==7):
                    window.cout_c("7 turns left")
                    window.cout_c("-------")
                    window.cout_c("  O    ")
                    window.cout_c("  |    ")
                elif(n==6):
                    window.cout_c("6 turns left")
                    window.cout_c("-------")
                    window.cout_c("  O    ")
                    window.cout_c("  |    ")
                    window.cout_c(" /     ")
                elif(n==5):
                    window.cout_c("5 turns left")
                    window.cout_c("-------")
                    window.cout_c("  O    ")
                    window.cout_c("  |    ")
                    window.cout_c(" / \   ")
                elif(n==4):
                    window.cout_c("4 turns left")
                    window.cout_c("-------")
                    window.cout_c("\ O    ")
                    window.cout_c("  |    ")
                    window.cout_c(" / \   ")
                elif(n==3):
                    window.cout_c("3 turns left")
                    window.cout_c("-------")
                    window.cout_c("\ O /  ")
                    window.cout_c("  |    ")
                    window.cout_c(" / \   ")
                elif(n==2):
                    window.cout_c("2 turns left")
                    window.cout_c("-------")
                    window.cout_c("\ O /- ")
                    window.cout_c("  |    ")
                    window.cout_c(" / \   ")
                elif(n==1):
                    window.cout_c("1 turn left")
                    window.cout_c("-------")
                    window.cout_c("\ O /_|")
                    window.cout_c("  |   ")
                    window.cout_c(" / \  ")
                elif(n==0):
                    window.cout_c("You lose. You let the kind man hang to death.")
                    window.cout_c("-----")
                    window.cout_c(" O_|")
                    window.cout_c("/|\  ")
                    window.cout_c("/ \  ")
                    window.cout_c("---------------------------------------------")
                    window.cout_c("The word is "+str)
                    window.cout_c("------------------------------------")
                    speech("You lose")
                    speech("You could not save the innocent man from dying")
            def hm():
                window.cout_c("------------------------------------")
                window.cout_c("WELCOME TO HANGMAN GAME")
                window.cout_c("Try to guess the word before I finish my drawing of Hanging the Man.")
                window.cout_c("You have 10 attempts to guess the word correctly")
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
                    app.processEvents()
                new.append(" ")
                while(True):
                    l=0
                    flag=0
                    lastflag=0
                    a=""
                    window.cout_c("")
                    window.cout_c("Guess the word :-")
                    for i in new:
                        a = a + i + " "
                        app.processEvents()
                    window.cout_c(a)

                    a=window.cin()

                    for i in word:
                        if(i==a):
                            new[l]=a
                            flag+=1
                        l+=1
                        app.processEvents()
                    if(flag==0):
                        count-=1
                        hang(count,str)
                        winsound.Beep(440, 800)
                    if(flag!=0):
                        window.cout_c("Right guess !")
                        speech("Right  guess")
                    for i in new:
                        if(i=="_ "):
                            lastflag+=1
                        app.processEvents()
                    if(lastflag==0):
                        window.cout_c("CONGRATULATIONS!!!  YOU WIN !!!... You have guessed the word right.You saved the kind man from being hanged")
                        window.cout_c("The word is "+str)
                        window.cout_c("------------------------------------")
                        speech("Congratulations")
                        speech("you saved the innocent man from dying")
                        break
                    if(count==0):
                        break 
                    app.processEvents() 
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
                a = ""
                window.cout_c("\n")
                window.cout_c("-------------------------")
                window.cout_c('   |   |   ')
                a =str(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
                window.cout_c(a)
                window.cout_c('   |   |   ')
                window.cout_c('-----------')
                window.cout_c('   |   |   ')
                a =str(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
                window.cout_c(a)
                window.cout_c('   |   |   ')
                window.cout_c('-----------')
                window.cout_c('   |   |   ')
                a =str(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
                window.cout_c(a)
                window.cout_c('   |   |   ')
                window.cout_c("------------------------")
                window.cout_c("\n")

            def IsWinner(b,l):
                return ((b[1]==l and b[2]==l and b[3]==l) or (b[4]==l and b[5]==l and b[6]==l) or
                        (b[7]==l and b[8]==l and b[9]==l) or (b[1]==l and b[4]==l and b[7]==l) or
                        (b[2]==l and b[5]==l and b[8]==l) or (b[3]==l and b[6]==l and b[9]==l) or
                        (b[1]==l and b[5]==l and b[9]==l) or (b[3]==l and b[5]==l and b[7]==l))

            def playerMove():
                while True:
                    window.cout_c("Please select a position to enter the X between 1 to 9 :- ")
                    speech("Please enter your move")
                    move = window.cin()
                    move = int(move)
                    window.cout_c("-----------")

                    try:
                        move = int(move)
                        if (move > 0 and move < 10):
                            if spaceIsFree(move):
                                insertLetter('X' , move)
                                break
                            else:
                                window.cout_c('Sorry, this space is occupied')
                                speech("The place is occupied")
                        else:
                            window.cout_c('Please type a number between 1 and 9 :-')
                            speech("Type a number between 1 and 9")

                    except:
                        window.cout_c('Please type a number')
                        speech("Please type a number")
                        playerMove()
                    app.processEvents()

            def computerMove():
                possibleMoves=[]
                for i in range(len(board)):
                    if(board[i]==' '):
                        possibleMoves.append(i)
                    app.processEvents()
                move=0

                for j in ['O','X']:
                    for i in possibleMoves:
                        boardcopy = board[:]
                        boardcopy[i]=j
                        if IsWinner(boardcopy,j):
                            move=i
                            return move
                        app.processEvents()
                    app.processEvents()

                if((board[1]=='X' and board[5]=='O' and board[9]=='X')or(board[3]=='X' and board[5]=='O' and board[7]=='X')):
                    edgesOpen=[]
                    for i in possibleMoves:
                        if i in [2,4,6,8]:
                            edgesOpen.append(i)
                        app.processEvents()
                    if len(edgesOpen)>0:
                        return random.choice(edgesOpen)
                    cornerOpen=[]
                    for i in possibleMoves:
                        if i in [1,3,7,9]:
                            cornerOpen.append(i)
                        app.processEvents()
                    if len(cornerOpen)>0:
                        return random.choice(cornerOpen)

                if 5 in possibleMoves:
                    move=5
                    return move

                cornerOpen=[]
                for i in possibleMoves:
                    if i in [1,3,7,9]:
                        cornerOpen.append(i)
                    app.processEvents()
                if len(cornerOpen)>0:
                    return random.choice(cornerOpen)

                edgesOpen=[]
                for i in possibleMoves:
                    if i in [2,4,6,8]:
                        edgesOpen.append(i)
                    app.processEvents()
                if len(edgesOpen)>0:
                    return random.choice(edgesOpen)

            def ttt():
                window.cout_c("\n")
                window.cout_c("WELCOME TO TIC-TAC-TOE")
                window.cout_c("------------------------------------------")
                speech("Welcome to tic tac toe")
                printBoard(board)
                while not(isBoardFull(board)):
                    if not(IsWinner(board,'O')):
                        playerMove()
                        printBoard(board)
                    else:
                        window.cout_c("You lose!")
                        speech("You lose")
                        break
                    
                    if not(IsWinner(board,'X')):
                        move=computerMove()
                        if(move==None or move==0):
                            window.cout_c("")
                        else:
                            insertLetter('O',move)
                            window.cout_c("Computer placed O in position ",move)
                            printBoard(board)
                            speech("Computer made is move in position"+str(move))
                    else:
                        window.cout_c("You win")
                        speech("Congratulations You win")
                        break
                    app.processEvents()
                    
                if isBoardFull(board):
                    window.cout_c("Tie game")
                    speech("The matched ended in a draw")
            ttt()
    
    #Dominos
    elif(c==12):
        # import PROJ_Dominos
        # PROJ_Dominos.pizza()
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
            speech("Listening")
            command = recognizer.recognize_once_async().get()

            if(command.reason == speechsdk.ResultReason.RecognizedSpeech):
                command = command.text
                command = command.strip()
                if(command[len(command)-1] == '.'):
                    command = command[slice(len(command)-1)]
                return command.lower()
            else:
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
                app.processEvents()
            while(len(phn_no)!=10):
                speech("Wrong phone number please try again")
                phn_no=inp()
                app.processEvents()

            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input'))).send_keys(phn_no)
            sleep(2)

            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input'))).click()
            sleep(2)

            speech("Enter otp")
            otp=inp()
            while(otp=="-1"):
                otp=inp()
                app.processEvents()
            while(len(otp)!=6):
                speech("Wrong otp please try again")
                otp=inp()
                app.processEvents()
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
                i = i+1
                app.processEvents()

            ss="ADD TO CART"
            dr=driver.find_elements(By.XPATH, "//span[contains(text(),'"+ss+"')]")
            addeditems = 0
            sleep(1)

            while(1<2):
                app.processEvents()
                speech("Enter your order")
                s=inp()
                #print(s)
                while(s=="-1"):
                    s=inp()
                    app.processEvents()

                res = s.split(',')

                for i in res:
                    i=i.strip()
                    app.processEvents()

                s = ' '.join(res)

                s=s.title()
                s=s.strip()
                x = difflib.get_close_matches(s, words)
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
                        app.processEvents()
                except:
                    speech("Not found")

                try:
                    driver.find_element(By.XPATH, "//span[contains(text(),'"+"NO THANKS"+"')]")
                    speech("do you want to add extra cheese")
                    i=inp()
                    i=i.strip()
                    i=i.lower()
                    while(i!="yes" and i!="no"):
                        speech("Wrong entry please try again")
                        i=inp()
                        app.processEvents()

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
                    app.processEvents()

                if(ch == "yes"):
                    speech("How many more items will you like to add ?")
                    cnt = int(inp())
                    for i in range(addeditems):
                        if(driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div['+str(i+1)+']/div/div/div[1]/div[2]/span[1]').text == s):
                            for j in range(cnt):
                                driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div['+str(i+1)+']/div/div/div[2]/div/div/div[2]/div').click()
                                sleep(1)
                                app.processEvents()
                        app.processEvents()
                else:
                    """"""


                speech("Do you want to add more items ?")
                ch = inp()
                while(ch == -1):
                    ch = inp()
                    app.processEvents()

                if(ch == "yes"):
                    continue
                else:
                    break
                app.processEvents()

                
            
                
                
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
                    app.processEvents()
                    
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

            sleep(10)

        pizza()
        window.cout_c("Thanks")

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
            window.cout_c("Task executed")
        google(URL)



def mnu():
    window.cout_c(        "---------------------------------------------------------------------------------------------------\nThe possible things you can tell to the virtual assistant\nMENU :-\nYoutube :- Play <something>                              Wikipedia :- Have the word 'wikipedia'\nDate :- today's date / current date                      Dictionary :- only type 'dictionary' first\nEmail :- Help me sending an email/send an email          Movies :- Suggest some movies\nWeather :- How is the weather today/today's weather      Game :- the keyword 'game'\nTime :- has the following keywords - time in <place>/    Songs :- recommend some songs/ recommend songs/\n        present time/ the time/ time now                          trending songs/ new songs/ old songs\nNews :- Today's headlines / today's news / news          Google :- Anything except these\nWill you like to order a pizza ? - Just ask <Order a pizza>\n--------------------------------------------------------------------------------------------------" + "\n")


#MAIN FUNCTION
mnu()
# speech("Hi")
# speech("I am Bishhokosh")
# speech("The menu for the works I can do is given below")

try:
    while(True):
        window.cout_c("Press t to search by typing or v for voice searching : ")
        x=window.cin()
        window.cout_c("------------")
        with urllib.request.urlopen("https://www.google.co.in") as response:
            input_command=-1
            if(x=='t'):
                input_command=input_type()
            elif(x=='v'):
                input_command=input_speech()
            else:
                window.cout_c("Wrong Input")
            if(input_command != -1):
                if(input_command.lower()=="exit" or input_command.lower()=="stop"):
                    window.cout_c("ADIOS AMIGO...POWERING OFF !")
                    speech("Adios amigo")
                    speech("Powering off")
                else:
                    search(input_command.lower(),x)
        app.processEvents()

except:
    window.cout_c("Can't provide any solution for that at the moment !")
    window.cout_c("ADIOS AMIGO...POWERING OFF !")
    speech("Can't provide any solution for that at the moment !")


app.exec()