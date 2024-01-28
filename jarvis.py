import sys

import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
from requests import get
import sys
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis, Please tell me how may i help you")
def take_command():
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
        # print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email-please', 'password-please')
    server.sendmail('email-please', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Aayush user\\Documents\\Audacity'
            songs = os.listdir(music_dir)
            if songs:
                random_song = random.choice(songs)
                song_path = os.path.join(music_dir, random_song)
                os.startfile(song_path)
            else:
                print("No songs found in the specified directory")
            print("songs")
            sys.exit()
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open py code' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.2.5\\bin\\pycharm64.exe"
            os.startfile(codePath)
        elif 'email to ayush' in query:
            try:
                speak("What should i say?")
                content = take_command()
                to = "email-please"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Aayush, I am not able to send this email")
        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif 'shutdown the system' in query:
            speak("Shutting down the system in 5 seconds. Save your work.")
            os.system("shutdown /s /t 5")
        elif 'restart the system' in query:
            speak("Restarting the system in 10 seconds. Save your work.")
            os.system("shutdown /r /t 10")
        elif 'no thanks' in query:
            speak("Thanks for using me. Have a good day sir")
            sys.exit()
        speak("Sir, do you have any other work")






