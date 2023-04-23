import json
from difflib import get_close_matches
import PROJ_Text_to_speech
import PROJ_Speech_to_text

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
        PROJ_Text_to_speech.speech("word not found")
        print("But we have got the closest match. Have a look at it")
        PROJ_Text_to_speech.speech("But we have got the closest match. Have a look at it")
        m=get_close_matches(x , data.keys())[0]
        print("The word :- ", m)
        return data[m]

def dict():
    print("Enter the word you need to search : ")
    PROJ_Text_to_speech.speech("Enter the word you need to search")
    x=PROJ_Speech_to_text.micro()
    print("")
    ans=check(x)
    PROJ_Text_to_speech.speech("Search Results found")
    c=1
    if(type(ans)==list):
        for i in ans:
            print(str(c)+"." , i)
            PROJ_Text_to_speech.speech("Number"+str(c))
            PROJ_Text_to_speech.speech(i)
            c+=1
        c=1
    else:
        print(ans)
    print("--------------------------------------------------------------------------------------------------")
    print("")

#dict()