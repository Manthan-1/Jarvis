import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechrecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import psutil

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The currect time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Hello Jarivs at your service!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and  hour<12:
        speak("Good Morning sir!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon sir!")
    elif hour >= 18 and  hour<24:
        speak("Good Evening sir!")
    else:
        speak("Good Night sir!")
   
    speak("How can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return"None"
    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender@mail', 'sender@password')
    server.sendmail('sender@mail', to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+ usage)
    battery = psutil.sensors_battery()
    speal("Battery is at"+ battery)

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query)
            print(result)   
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = 'receiver@mail'
                sendEmail(to, content)
                speak("Email has been sent....")

            except Exception as e:
                print(e)
                speak("Unable to send the mail, sorry...")

        elif 'search in chrome' in query:
            speak("What should i search?")
            cp = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            search = takeCommand().lower()
            wb.get(cp).open_new_tab(search+'.com')


        elif 'logout' in query:
            os.system("shutdown -1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("restart /r /t 1")

        elif 'play songs' in query:
            songs_dir = 'E:\Songs'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0])) 

        elif 'remember' in query:
            speak("what should i recall??")
            data = takeCommand()
            speak("You asked me to recall"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()


        elif 'cpu' in query:
            cpu() 
            
        elif 'offline' in query:
            quit()
            
        