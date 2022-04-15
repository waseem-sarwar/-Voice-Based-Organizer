# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 00:36:09 2022

@author: dell 3510
"""

import speech_recognition as sr
import pyttsx3
import pyaudio 

ngin = pyttsx3.init()
voices = ngin.getProperty('voices')
ngin.setProperty('voices', voices[0].id)

def speak(text):
    ngin.say(text, name="footman")
    ngin.runAndWait()
    
    
listener = sr.Recognizer()
listener.energy_threshold = 50

for index, name in enumerate(sr.Microphone.list_microphone_names()):
      print("Microphone with name \"{1}\" found for Microphone(device_index={0})".format(index, name))

print("If you see a microphone that matches its name in your volume settings, then the microphone is being discovered. PLease note the device_index to replace in sr.Microphone()")


def listening(source):
     print('Adjusting...')
     listener.adjust_for_ambient_noise(source, duration=3)
     print('Listening...')
     voice = listener.listen(source, phrase_time_limit=20)
     print("Recognizing...")
     return listener.recognize_google(voice)
 
try:
    with sr.Microphone(device_index=1) as source:
        command = listening(source)
        command = command.lower()
        print(command)
        speak("If you have encountered no errors up till this point, and you see the text that you spoke, then the code should work correctly.")
        
except:
    print("If nothing was printed, there might be something wrong with the mic.")
    pass

