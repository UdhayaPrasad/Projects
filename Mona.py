import pyttsx3
import speech_recognition as sr
import pywhatkit
from googlesearch import search
import webbrowser
import os
from datetime import date
from googletrans import Translator
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',145)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
   

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
   r=sr.Recognizer()
   with sr.Microphone() as source:
    print("Say Something..")
    print("Am Listening.......")
    try:
       audio=r.listen(source)
       text=r.recognize_google(audio)
       print(text)
       return text
    except Exception as e:
        print("Error while listening... Unable to listen")
    
   
def sendmsg():
    speak('Enter the Mobile NUmber u want send message')
    mobileno=input("Enter the Mobile NUmber:")
    speak("Enter the Message you want to send:")
    msg=input("Enter the Message:")
    pywhatkit.sendwhatmsg(mobileno,msg,15,41)
    speak("Message sent Successfully!!!!")

def youtube():
    speak("What kind of song you want to play:")
    songname=listen()
    speak("Playing"+songname+"on youtube..")
    pywhatkit.playonyt(songname)

def search():
    speak("What should i search on google")
    topic=listen().replace("/", "")
    speak("Ok boss opening"+topic+"on google")
    webbrowser.open("https://www.google.com/search?q="+topic)


def translate():
    # Placeholder for the speak() function
    speak('Ok boss, speak to translate your speech')
    text = listen()  # Placeholder for the listen() function
    speak("Speech Captured Successfully")
    speak("Which language do you want to translate to?")
    language = listen()  # Placeholder for the listen() function

    if language.lower() == "english":
        language_code = "en"
    elif language.lower() == "tamil":
        language_code = "ta"
    else:
        # Handle unrecognized language
        speak("Sorry, I can only translate to English and Tamil at the moment.")
        return

    translator = Translator()
    translated_text = translator.translate(text, dest=language_code)
    return translated_text

def SendMail():
   try:
      sender_mail="Udhay2024@outlook.com"
      password='Shiva@2024'
      speak("Enter the Mail ID of the student:")
      reciever_mail=input("Enter the mail id of the student:")  
      speak("Enter the subject for Mail:")
      subject=input("Enter the subject:")
      speak("Enter the Message for Mail:")
      Message=input("Enter the message:")
      
      m=MIMEText(Message)
      m['subject']=subject
      server=smtplib.SMTP('smtp-mail.outlook.com',587)
      server.starttls()
      server.login(user=sender_mail,password=password)
      speak("Login Successful..")
      
      server.sendmail(sender_mail,reciever_mail,msg=m.as_string())
      server.quit()
      speak("Sent mail successfully")
     
   except Exception as e:
      print("Error while sending mail")


speak('HI THIS IS MONA YOUR PERSONAL ASSISTANT .... ')
speak("How can i help you today....")
talk=True

while talk:
 
 command=listen()
 if 'send message' in command:
      speak("Ok Boss sending message")
      sendmsg()

 if'song' in command:
     speak("Ok Boss playing")
     youtube()

 if'search'in command:
    search()

 if 'open Microsoft' in command:
   speak("ok Boss opening microsoft")
   os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk")

 if'translate' in command:
    t=translate()
    speak("Translated Text:"+t)

 if'send mail'in command:
    SendMail()
 if'Bye' in command:
    talk=False
    speak("Am Happy to help u today see u later.. Bye Have a nice day")

    
    


  





