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