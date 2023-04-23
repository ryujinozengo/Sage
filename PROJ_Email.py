import azure.cognitiveservices.speech as speechsdk # for speech recognition
import smtplib # for email server
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import PROJ_Text_to_speech

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
                PROJ_Text_to_speech.speech("Nothing Recognnized Please type in")
                return input()


        sender = "legtgsrk613@gmail.com"
        print("Type in the receiver email address : ")
        PROJ_Text_to_speech.speech("Type in the receiver email address")
        receiver = input()

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver

        print("Enter subject : ")
        PROJ_Text_to_speech.speech("Enter subject")
        if(x=='t'):
            msg['Subject'] = input()
        else:
            msg['Subject'] = input_speech()

        print("Enter body : ")
        PROJ_Text_to_speech.speech("Enter body")
        if(x=='t'):
            body = input()
        else:
            body = input_speech()
        msg.attach(MIMEText(body, 'plain'))

        print("Enter file name : ")
        PROJ_Text_to_speech.speech("Enter file name")
        filename = input()
        if(filename.lower() != "none"):
            print("Enter path : ")
            PROJ_Text_to_speech.speech("Enter path")
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
        #s.login(sender, "raraoxhuyinyeszj")
        text = msg.as_string()
        s.sendmail(sender, receiver, text)
        s.quit()
        print("Email sent!")
        PROJ_Text_to_speech.speech("Email sent")
    
    except:
        print()
        print("------------------------------------------------------------------------")
        print("You are either not connected to internet or the receiver email address")
        print("could not be found or the file name/location may have some errors.")
        print("Please try again")
        print("------------------------------------------------------------------------")

# email_sender('v')