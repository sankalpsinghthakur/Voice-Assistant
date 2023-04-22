import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


#setting up the voice

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wishes you with keeping the time of the day in mind

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>0 and hour <12:
        speak("good morning!")
    elif  hour>=12 and hour <18:
        speak("good Afternoon!")
    else :
        speak("good evening!")
    speak("I am Reyna,  Please tell me how can i help you")

#It takes input from microphone and returns string output

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recogninzing...")  
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"   
    return query
#sending email
#you have to allow less secure apps in your google account to send email
def sendEmail(to,content):
    server = smtplib.SMPT('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your@gmail.com', 'your-password')
    server.sendmail('your@gmail.com',to,content)
    server.close()


#main code

if __name__=="__main__":
     wishMe()

#while True:
query= takeCommand().lower()

# executing tasks based on query

if 'wikipedia' in query:
    print('Searching wikipedia...')
    speak('Searching wikipedia...')
    query = query.replace("wikipedia", "")

# you can change how much lines of results in sentence =2

    results = wikipedia.summary(query, sentences=2)
    speak("According to wikipedia")
    print(results)
    speak(results)

# any sites you want REyna to open for you

elif 'open youtube' in query :
    webbrowser.open("youtube.com")
elif 'open google' in query :
    webbrowser.open("google.com")
elif 'open github' in query :
    webbrowser.open("github.com")

# for playing music
#set the directory according to you

elif 'play music' in query:
    music_dir= 'D:\\music'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir,songs[1]))

# for knowing the time    

elif 'the time' in query:
    strTime =  datetime.datetime.now().strftime("%H:%M:%S")  
    speak(f"Sir, the time is{strTime}")

#to open any application or file copy its targetpath    

elif 'open picture' in query:
    picPath= "C:\\Users\\Sankalp Singh Thakur\\OneDrive\\Desktop\\python\\Reyna-Assistant\\9.jpg"
    os.startfile(picPath)  

#sending email
elif 'email to sankalp' in query:
    try:
        speak("what should i say ?")
        content = takeCommand()
        to = "your@gmail.com"
        sendEmail(to,content)
        speak("Email has been sent!")
    except Exception as e:
        print (e)
        speak("sorry unable to send email")


        
##########################################################
# by SANKALP SINGH THAKUR        