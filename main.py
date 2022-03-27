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
    with sr.Microphone() as source:
        print('Listening')
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio = r.listen(source)
        try:
            print("Recognizing")
            command = r.recognize_google(audio)
        except Exception as e:
            print(e)
            return "None"

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
        command = cmd().lower()

        if "open youtube" in command:
            speak("Opening youtube ")
            webbrowser.open("www.youtube.com")
            continue

        elif "open browser" in command:
            speak("Opening Google Chrome ")
            webbrowser.open("www.google.com")
            continue

        elif "open instagram" in command:
            speak("your instagram is Opening")
            webbrowser.open("https://www.instagram.com")
            continue

        elif "open email" in command:
            speak("your email is Opening")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            continue

        elif "open whatsapp" in command:
            speak("your whatsapp is Opening ")
            webbrowser.open("https://web.whatsapp.com")
            continue

        elif "open translate" in command:
            speak("Opening translate")
            webbrowser.open("https://translate.google.co.ma/?hl=fr")
            continue

        elif "open github" in command:
            speak("your github is Opening")
            webbrowser.open("https://github.com/AbdessamadBaali")
            continue

        elif "what day is it" in command:
            dayCurrnt = datetime.datetime.now().strftime('%A')
            speak(f"to day is  {dayCurrnt}" )
            continue

        elif "what year are we" in command:
            dayCurrnt = datetime.datetime.now().strftime('%Y')
            speak(f"we are in {dayCurrnt}" )
            continue

        elif "what month are we" in command:
            dayCurrnt = datetime.datetime.now().strftime('%B')
            speak(f"we are in {dayCurrnt}" )
            continue

        elif "tell me the time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"the current time is {time}" )
            continue

        elif "tell me the full date" in command:
            time = datetime.datetime.now().strftime('%Y %B %A %I:%M %p')
            speak(f"the full date is {time}" )
            continue

        elif 'play' in command:      
            print(command)
            song = command.replace('alexa','')
            speak("ok the vedio will play please wait a second")
            pywhatkit.playonyt(song)
            continue

        elif "from wikipedia" in command:
            print(command)
            speak("Checking the wikipedia please wait a second ")
            command = command.replace("wikipedia", "")
            result = wikipedia.summary(command, sentences=3)
            speak("According to wikipedia")
            speak(result)

        elif "who  is" in command:
            print(command)
            speak("please wait a second ")
            command = command.replace("how is", "")
            result = wikipedia.summary(command, sentences=3)
            speak(result)

        elif 'search' in command:
            command = command.replace('search', '')
            command = command.replace('alexa', '')
            pywhatkit.search(command)
            speak("Searching Result in Google!")
            continue

        elif "your name" in command:
            speak("I am alexa. Your Virtual Assistant!")
            continue

        elif "how are you doing" in command:
            speak("i am doing great! thank for asking")


        elif 'what are you doing' == command:
            speak("nothing")

        elif 'thank you alexa' == command:
            speak("no need to think me- i'm Your Virtual Assistant!")

        elif 'alexa' == command:
            speak("yes sir, what can i do for you")

        elif 'say' in command:
            command = command.replace("say", '')
            command = command.replace("alexa", '')
            speak(command)

        elif 'joke' in command:
            speak(pyjokes.get_joke())
            continue

        elif 'close' in command:
            command = command.replace('close', '')
            command = command.replace('alexa', '')
            print(command)
            os.system(f"taskkill/im {command}.exe")
            speak('the programme is closed!')
            continue

        elif "goodbye" in command:
            speak("Good Bye !")
            exit()
            
take_cmd()