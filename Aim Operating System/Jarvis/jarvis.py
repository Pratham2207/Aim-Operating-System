import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import random
import datetime
import os
import datef

random = ("good evening sir, how was your day")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning sir, aim online")
        elif hour >= 12 and hour < 18:
                speak("Good Afternoon sir, aim here")
        else:
                     speak (random)


def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)
        try:
            print("Recognising")
            text = r.recognize_google(audio,language='en-in')
            print(text)
        except Exception:
             speak("error....")
             print("Network error")
             return "none"
        return text
                
    

if __name__ == "__main__":
            wish()
            while True:
                query  = takecom().lower()
                
                if "wikipedia" in query:
                    speak("Searching details.....Please Wait")
                    query.replace("wikipedia","")
                    results = wikipedia.summary(query,sentences=2)
                    print(results)
                    speak(results)
                elif 'open youtube' in query or "open video online" in query:
                        webbrowser.open("www.youtube.com")
                        speak("open youtube")
                elif 'open google' in query or "search google" in query:
                        webbrowser.open("www.google.co.in")
                        speak("opening google")
                elif 'bye' in query or 'shutdown'in query or 'quit'in query:
                        speak("Bye sir, aim going offline")
                        exit()
                elif "shutdown operating system" in query:
                        speak("Ok sir. Shutting down the system")
                        os.system('shutdown -s')
                elif 'open github' in query:
                    webbrowser.open("google.com.github.com")
                    speak("Yes sir, opening your github")
                elif 'open facebook' in query:
                    speak("Ok sir, opening facebook")
                    webbrowser.open("http://www.facebook.com/")
                elif 'open white hat' in query:
                    speak("opening whitehat")
                    webbrowser.open("https://www.whitehatjr.com/")
                elif'who are you' in query:
                    speak("I am aim, a programme created by mister bajajj, aim stands for artificial intelligence machine")
                elif 'what can you do'in query:
                    speak("I can open many websites and open applications like vs code and can search anything for you, in wikipedia")
                elif 'open vs code' in query:
                    speak("opening vs code")
                    codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
                elif 'set alarm'in query:
                    speak("ok sir, your alarm has started")
                    datef.alarm(query)
                    speak("sir, your time is up")
                elif  'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir,the time is {strTime}")
                elif 'open meet'in query or 'start meet'in query:
                    speak("yes sir, starting meet")
                    webbrowser.open("meet.google.com")
                elif 'open class'in query or 'open gc'in query:
                    speak("ok sir, opening google classroom")
                    webbrowser.open("https://classroom.google.com/u/1/c/OTYwMDU0NjE5NDha")
                elif 'nice day'in query or 'great day'in query or 'best day'in query:
                    speak("good to hear that sir, how may i help you?")
                elif 'mail'in query:
                    speak("sure sir, opening mail")
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                elif 'thanks'in query or 'thank you'in query:
                    speak("your most welcome sir")
                elif 'open your system'in query:
                    speak("ok sir, opening my operating system")
                    codePath = "C:\\Users\\DELL\\Desktop\\AIM"
                    os.startfile(codePath)
                elif'open my achievements'in query:
                    speak("ok sir, opening your trophies")
                    codePath = "C:\\Users\\DELL\\Desktop\\WHJ Achievments"
                    os.startfile(codePath)
                elif 'open my works'in query:
                    speak("opening your works folder")
                    codePath = "C:\\Users\\DELL\\Desktop\\WhiteHatJr Work"
                    os.startfile(codePath)
                elif 'open chrome'in query or 'open google chrome'in query:
                    speak("sure sir, opening chrome")
                    codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(codePath)
                elif'open edge'in query:
                    speak("opening microsoft edge")
                    codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                    os.startfile(codePath)
                elif 'drive'in query:
                    speak("opening google drive")
                    webbrowser.open("https://drive.google.com/drive/u/0/my-drive")
                elif 'git'in query:
                    speak("opening your git bash")
                    codePath = "C:\\Program Files\\Git\\git-bash.exe"
                    os.startfile(codePath)
                elif'firefox'in query:
                    speak("sure sir, opening firefox")
                    codePath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
                    os.startfile(codePath)
                
               
