import random
import winsound
import PROJ_Text_to_speech

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
        PROJ_Text_to_speech.speech("You lose")
        PROJ_Text_to_speech.speech("You could not save the innocent man from dying")
def hm():
    print("------------------------------------")
    print("WELCOME TO HANGMAN GAME")
    print("Try to guess the word before I finish my drawing of Hanging the Man.")
    print("You have 10 attempts to guess the word correctly")
    PROJ_Text_to_speech.speech("welcome to hangman")
    PROJ_Text_to_speech.speech("You have 10 attempts to guess the word else the innocent man will be hanged to death")

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
            PROJ_Text_to_speech.speech("Right  guess")
        for i in new:
            if(i=="_ "):
                lastflag+=1
        if(lastflag==0):
            print("CONGRATULATIONS!!!  YOU WIN !!!... You have guessed the word right.You saved the kind man from being hanged")
            print("The word is",str)
            print("------------------------------------")
            PROJ_Text_to_speech.speech("Congratulations")
            PROJ_Text_to_speech.speech("you saved the innocent man from dying")
            break
        if(count==0):
            break

#hm()