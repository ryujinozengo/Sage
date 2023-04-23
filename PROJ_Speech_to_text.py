import time
import speech_recognition as sr
import azure.cognitiveservices.speech as speechsdk

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

def google():
    r = sr.Recognizer()
    r.energy_threshold = 300
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")    
            aud = r.recognize_google(audio, language="en-IN")
            print(aud)
        except Exception as e:
            print(e)    
            print("Say that again please...")
            
def micro_cont():
    listener = speechsdk.SpeechConfig(subscription="8ef9bc73c3914aaa9cc945229520fb66", region="centralindia")
    listener.speech_recognition_language="en-IN"
    receiver = speechsdk.audio.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.SpeechRecognizer(speech_config=listener, audio_config=receiver)
    print("Listening")

    command = ""
    c = -1
    done = False
    def stop_cb(evt):
        print('CLOSING on {}'.format(evt))
        recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    def concat_command(evt):
        nonlocal command 
        command = command + evt + " "

    recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    recognizer.recognized.connect(lambda evt: stop_cb(evt) if((str(evt)[153:-42]).lower() == "stop") else concat_command(str(evt)[153:-42]))
    recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(str(evt)[153:-42])))
    c += 1
    recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    recognizer.canceled.connect(lambda evt: print('CANCELLED {}'.format(evt)))
    
    recognizer.session_stopped.connect(lambda evt: stop_cb if(evt == "Stop.") else None)
    recognizer.canceled.connect(stop_cb)

    recognizer.start_continuous_recognition()
    while not done:
        time.sleep(0.5)
    
    print(command)
 
 
def micro_cont_2():
    while True:
        listener = speechsdk.SpeechConfig(subscription = "8ef9bc73c3914aaa9cc945229520fb66", region = "centralindia")
        #listener = speechsdk.SpeechConfig(subscription = "bad56e16463a403dad64f587c55e4d81", region = "centralindia")
        listener.speech_recognition_language = "en-IN"
        receiver = speechsdk.audio.AudioConfig(use_default_microphone = True)
        recognizer = speechsdk.SpeechRecognizer(speech_config = listener, audio_config = receiver)
        print("Listening(microsoft)...")
        command = recognizer.recognize_once_async().get()
        if(command.reason == speechsdk.ResultReason.RecognizedSpeech):
            command = command.text
            command = command.strip()
            if(command[len(command)-1] == '.'):
                command = command[slice(len(command)-1)]
            print(command.lower())
            continue
            return command.lower()
        else:
            print("Nothing Recognized")
            continue     

#micro_cont_2()
#micro_cont()
#micro()
#google()