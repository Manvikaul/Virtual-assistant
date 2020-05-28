# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:24:13 2020

@author: DELL
"""

'''
Dependencies required:
    pip install pyaudio
    pip install SpeechRecognition
    pip install gTTs
    pip install wikipedia
'''

#importing libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import playsound

#Ignore warning messages
warnings.filterwarnings('ignore')

#Record audio and return it as a string
def recordAudio():
    
    #Record the audio
    r=sr.Recognizer()
    #open the mic and start rec
    with sr.Microphone() as source:
        print('Say something')
        audio=r.listen(source)
        
    #using google's speech recognition
    data=''
    try:
        data=r.recognize_google(audio)
        print('You said '+data)
        
    except sr.UnknownValueError:
        print('Google speach reconignition could not understand, Unknown error')
    except sr.RequestError as e:
        print('Connection error: '+ e)
        
    return data

#recordAudio()
    
#getting virtual assistant's response
def assistantResponse(text):
    print(text)
    #convert text to speech
    myobj=gTTS(text=text,lang='en',slow=False)
    #save audio
    myobj.save('assistant_response.mp3')
    #play audio
    playsound.playsound('assistant_response.mp3',True)
    os.remove('assistant_response.mp3')
    
#text='this is a test'
#assistantResponse(text)
    
#Setting wake words
def wakeWord(text):
   WAKE_WORDS=['hey computer','okay computer'] 
   
   text=text.lower()
   for phrase in WAKE_WORDS:
       if phrase in text:
           return True
       
   return False


#Getting the date
def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]
    monthNum=now.month
    dayNum=now.day
    
    month_names=['January','February','March','April','May','June','July','August','September'
                 'October','November','December']
    ordinal_numbers=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th',
                     '13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd',
                     '23rd','24th','25th','26th','27th','28th','29th','30th','31st']
    
    return 'Today is '+ weekday +', '+ month_names[monthNum-1] + ' the '+ ordinal_numbers[dayNum-1]+'.'

#print(getDate())


#Returning random greeting response
GREETING_INPUTS=['hey','hi','hello','heya','howdy','whatsup','wassup','hola']
GREETING_OUTPUTS=['hey!','hello!','heya!','howdy!','hey there!','holaa!']

def greeting(sentence):
  for word in sentence.split():
    if word.lower() in GREETING_INPUTS:
      return random.choice(GREETING_OUTPUTS)+'.'
  return ''

def  getPerson(text):
    wordList=text.split()
    
    for i in range(0,len(wordList)):
        if i+3 <= len(wordList)-1 and wordList[i].lower()=='who' and wordList[i+1].lower()=='is':
            return wordList[i+2]+' '+wordList[i+3]

#Recording the audio        
while True:
    text=recordAudio()
    response=''
    
    if(wakeWord(text)==True):
        response=response+greeting(text)
        
        if 'date' in text:
            getDate=getDate()
            response=response+' '+getDate
            
        if 'time' in text:
            now=datetime.datetime.now()
            suffix=''
            if now.hour>=12:
                suffix='p.m'
                hour=now.hour-12
            else:
                suffix='a.m'
                hour=now.hour
                
            if now.minute<10:
                minute='0'+str(now.minute)
            else:
                minute=str(now.minute)
                
            response=response+' '+'It is '+str(hour)+':'+minute+' '+suffix+'.'
            
        if 'who is' in text:
            person=getPerson(text)
            wiki=wikipedia.summary(person,sentences=2)
            response=response+' '+wiki
            
            assistantResponse(response)
    
    
   
#text='what is the date and who is sherlock holmes'
#person=getPerson(text)
#wiki=wikipedia.summary(person,sentences=2)
#response=''
#getDate=getDate()
#response=response+' '+getDate
#response=response+' '+wiki
#assistantResponse(response)


    
    
    
    
    
    
    
    