import random
from pygame import mixer
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pyttsx3
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 200)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1.0)


wishes = ["Good luck and good wishes", "You’re going to be amazing", "Hope you’re feeling good and confident about today", "All your hard work is about to pay off",
          "Go out and give it your best shot", "Just relax and do your best. You’ll be great", "Sending you good-luck hugs", "Best of luck today", "Good luck! I believe in you", "I hope this good-luck candy bar gives you a little extra boost"]

birthday_wish = ["Lots of wishes for your birthday. May you have an incredible day and a stunning night.",
                 "I wish everything you get on the day remain colorful, sweet and bright. May you have an eidetic memory birthday night "]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    speak("I am your Assistant Jarvis")
    speak("How can i Help you")


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


if __name__ == '__main__':
    def clear(): return os.system('cls')
    clear()

    while True:
        command = takeCommand().lower()

        if "wish" in command:
            if "luck" in command:
                wish = random.choice(wishes)
                speak(wish)
            elif "birthday" in command:
                bday = random.choice(birthday_wish)
                speak(bday)
                mixer.init()
                mixer.music.load("bday_song.mp3")
                mixer.music.set_volume(0.7)
                mixer.music.play()
            else:
                wishMe()
        elif "shutdown" in command or "exit" in command:
            exit()
        elif "birthday" in command:
            bday = random.choice(birthday_wish)
            speak(bday)
            mixer.init()
            mixer.music.load("bday_song.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()
        elif "open youtube" in command:
            webbrowser.open("http://youtube.com", new=0)
        elif "open google" in command:
            webbrowser.open("http://google.com", new=0)
        elif "open wikipedia" in command:
            webbrowser.open("http://wikipedia.com", new=0)
        elif "open gmail" in command:
            webbrowser.open("http://gmail.com", new=0)
        elif "play my favourite song" in command:
            webbrowser.open(
                "https://www.youtube.com/watch?v=6J8ph0LGnIE", new=0)
        elif "search" in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'date' in command or 'year' in command or 'month' in command:
            strTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            speak(f"Date and time is {strTime}")
        elif 'how are you' in command:
            speak("I am fine, Thank you")
        elif 'fine' in command or "good" in command:
            speak("It's good to know that your fine")
        elif "what's your name" in command or "What is your name" in command:
            speak("my name in jarvis, at your service")
        elif 'joke' in command:
            speak(pyjokes.get_joke())
        elif 'show me about' in command:
            command = command.replace("search", "")
            webbrowser.open(command, new=0)
        else:
            speak("please say it clearly")
