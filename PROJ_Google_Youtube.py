import webbrowser # for google search
import pywhatkit # for youtube search

#Search on youtube
def youtube(ic):
    pywhatkit.playonyt(ic)
    print("Task executed")

#search on google
def google(url):
    webbrowser.open_new_tab(url)
    print("Task executed")

#google("http://www.google.com")
#youtube("play sultan kgf")