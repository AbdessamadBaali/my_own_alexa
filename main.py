# text to speech library
import pyttsx3
# library convert audio into text
import speech_recognition as sr
# library to display Web-based documents to users
import webbrowser
# library to fetch current date and time
import datetime
# library to fetch wikipedia information
import wikipedia
# library to play youtube video and perform google search
import pywhatkit
# library that is used to create one-line jokes
import pyjokes
import os

# method to accept and recognize commands given by the user
def cmd():
    # create speech_recognition
    r = sr.Recognizer()
    m = sr.Microphone()
    sr.Microphone.list_microphone_names()

    with m as source:
        print("listing")
        r.adjust_for_ambient_noise(source, duration=.8)
        audio = r.listen(source,  phrase_time_limit=3)
    
        try:
            print("Recognizing")
            command = r.recognize_google(audio)
        finally:
            return command

# speatk method 
def speak(audio):
    global engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine. setProperty("rate", 178)
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

# greating robot alexa
def welcome():
    speak('Hello!!! I am alexa  your desktop assistant.')

# tacke command method and do the command if exists
def take_cmd():
    welcome()
    while (True):
        engine. setProperty("rate", 120)
        global cmd_To_Do
        cmd_To_Do = cmd().lower()

        if "open youtube" in cmd_To_Do:
            speak("Opening youtube ")
            webbrowser.open("www.youtube.com")
            continue

        elif "open browser" in cmd_To_Do:
            speak("Opening Google Chrome ")
            webbrowser.open("www.google.com")
            continue

        elif "open instagram" in cmd_To_Do:
            speak("your instagram is Opening")
            webbrowser.open("https://www.instagram.com")
            continue

        elif "open email" in cmd_To_Do:
            speak("your email is Opening")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            continue

        elif "open whatsapp" in cmd_To_Do:
            speak("your whatsapp is Opening ")
            webbrowser.open("https://web.whatsapp.com")
            continue

        elif "open translate" in cmd_To_Do:
            speak("Opening translate")
            webbrowser.open("https://translate.google.co.ma/?hl=fr")
            continue

        elif "open github" in cmd_To_Do:
            speak("your github is Opening!")
            webbrowser.open("https://github.com/AbdessamadBaali")
            continue

        elif "what day is it" in cmd_To_Do:
            dayCurrnt = datetime.datetime.now().strftime('%A')
            speak(f"to day is  {dayCurrnt}" )
            continue

        elif "what year are we" in cmd_To_Do:
            dayCurrnt = datetime.datetime.now().strftime('%Y')
            speak(f"we are in {dayCurrnt}" )
            continue

        elif "what month are we" in cmd_To_Do:
            dayCurrnt = datetime.datetime.now().strftime('%B')
            speak(f"we are in {dayCurrnt}" )
            continue

        elif "tell me the time" in cmd_To_Do:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"the current time is {time}" )
            continue

        elif "tell me the full date" in cmd_To_Do:
            time = datetime.datetime.now().strftime('%Y %B %A %I:%M %p')
            speak(f"the full date is {time}" )
            continue

        elif 'play' in cmd_To_Do:      
            print(cmd_To_Do)
            song = cmd_To_Do.replace('alexa','')
            speak("ok the vedio will play please wait a second")
            pywhatkit.playonyt(song)
            continue

        elif "from wikipedia" in cmd_To_Do:
            print(cmd_To_Do)
            speak("Checking the wikipedia please wait a second ")
            cmd_To_Do = cmd_To_Do.replace("wikipedia", "")
            result = wikipedia.summary(cmd_To_Do, sentences=3)
            speak("According to wikipedia")
            speak(result)

        elif "who is" in cmd_To_Do:
            speak("please wait a second ")
            cmd_To_Do = cmd_To_Do.replace("how", "")
            cmd_To_Do = cmd_To_Do.replace("is", "")
            result = wikipedia.summary(cmd_To_Do, sentences=3)
            speak(result)

        elif 'search' in cmd_To_Do:
            cmd_To_Do = cmd_To_Do.replace('search', '')
            cmd_To_Do = cmd_To_Do.replace('alexa', '')
            pywhatkit.search(cmd_To_Do)
            speak("Searching Result in Google!")
            continue

        # tell alexa to say something
        elif 'alexa say' in cmd_To_Do:
            cmd_To_Do = cmd_To_Do.replace("say", '')
            cmd_To_Do = cmd_To_Do.replace("alexa", '')
            speak(cmd_To_Do)

        elif "your name" in cmd_To_Do:
            speak("I am alexa. Your Virtual Assistant!")
            continue

        elif "how are you doing" in cmd_To_Do:
            speak("i am doing great! thank for asking")


        elif 'what are you doing' in cmd_To_Do:
            speak("nothing")

        elif 'thank you' in cmd_To_Do:
            speak("no need to think me- i'm Your Virtual Assistant!")

        elif 'alexa' == cmd_To_Do:
            speak("yes sir, what can i do for you")

        # tell alexa to say a joke
        elif 'joke' in cmd_To_Do:
            speak(pyjokes.get_joke())
            continue
        
        # tell alexa to colse  a  programme 
        elif 'close' in cmd_To_Do:
            cmd_To_Do = cmd_To_Do.replace('close', '')
            cmd_To_Do = cmd_To_Do.replace('alexa', '')
            print(cmd_To_Do)
            os.system(f"taskkill/im {cmd_To_Do}.exe")
            speak('the programme is closed!')
            continue 

        # close the browser
        elif 'close browser' in cmd_To_Do:           
            os.system(f"chrome.exe")
            speak('the programme is closed!')
            continue 

        # open a programme
        elif 'open' in cmd_To_Do:
            cmd_To_Do = cmd_To_Do.replace('open', '')
            pyttsx3.speak(f"{cmd_To_Do} is Opening")
            os.system(cmd_To_Do)
            continue

        # open microsoft edge
        elif ("id" in cmd_To_Do) or ("msedge" in cmd_To_Do) or ("edge" in cmd_To_Do):
            pyttsx3.speak("MICROSOFT EDGE is Opening")
            os.system("msedge")
            continue
    
        # open microsoft edge
        elif ("not" in cmd_To_Do) or ("notepad" in cmd_To_Do) or ("editor" in cmd_To_Do):
            pyttsx3.speak("NOTEPAD is Opening")
            os.system("Notepad")
            continue

        # open microsoft excel
        elif ("excel" in cmd_To_Do) or ("msexcel" in cmd_To_Do) or ("winexcel" in cmd_To_Do):
            pyttsx3.speak("Opening MICROSOFT EXCEL")
            os.system("excel")
            continue
    
        # open powerpoint
        elif ("powerpoint" in cmd_To_Do) :
            pyttsx3.speak("Opening MICROSOFT POWERPOINT")
            os.system("powerpnt")
            continue
        
        # open microsoft word
        elif "microsoft word" in cmd_To_Do:
            pyttsx3.speak("Opening MICROSOFT WORD")
            os.system("winword")
            continue
    
        # close the program
        elif ("goodbye" in cmd_To_Do):
            pyttsx3.speak("Good Bye !")
            break
        print(cmd_To_Do)

take_cmd()