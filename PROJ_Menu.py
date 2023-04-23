import PROJ_Text_to_speech
from modules import *

def mnu(self):
    self.coutc(        "---------------------------------------------------------------------------------------------------\nThe possible things you can tell to the virtual assistant\nMENU :-\nYoutube :- Play <something>                              Wikipedia :- Have the word 'wikipedia'\nDate :- today's date / current date                      Dictionary :- only type 'dictionary' first\nEmail :- Help me sending an email/send an email          Movies :- Suggest some movies\nWeather :- How is the weather today/today's weather      Game :- the keyword 'game'\nTime :- has the following keywords - time in <place>/    Songs :- recommend some songs/ recommend songs/\n        present time/ the time/ time now                          trending songs/ new songs/ old songs\nNews :- Today's headlines / today's news / news          Google :- Anything except these\nWill you like to order a pizza ? - Just ask <Order a pizza>\n--------------------------------------------------------------------------------------------------" + "\n")
    PROJ_Text_to_speech.speech("Hi")
    PROJ_Text_to_speech.speech("I am Bishhokosh")
    PROJ_Text_to_speech.speech("The menu for the works I can do is given below")


def moviemnu():
    print("\nChoose from the given list of type of movies :\n")
    print("1. TOP 250 movies of all time")
    print("2. Popular")
    print("3. All time box office movies")
    print("4. In theatres now")
    print("5. Coming soon")
    print("\nEnter your choice")

#mnu()
#moviemnu()