# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 02:06:30 2022

@author: dell 3510
"""

import speech_recognition as sr
import pyttsx3
import pyaudio 

listener = sr.Recognizer()
listener.energy_threshold = 50

ngin = pyttsx3.init()
voices = ngin.getProperty('voices')
ngin.setProperty('voices', voices[0].id)


def speak(text):
    ngin.say(text, name="footman")
    ngin.runAndWait()

for index, name in enumerate(sr.Microphone.list_microphone_names()):
      print("Microphone with name \"{1}\" found for Microphone(device_index={0})".format(index, name))

while(1):
    try:
        with sr.Microphone(device_index=1) as source:
            print('Adjusting.')
            listener.adjust_for_ambient_noise(source, duration=3)
            print('Listening...')
            voice = listener.listen(source, phrase_time_limit=40)
            print("Recognizing...")
            command = listener.recognize_google(voice, language="en-UK")
            
            command = command.lower()
            print(command)
            speak(command)
    except sr.UnknownValueError:
        print("Unknown value!")        
        pass
    except sr.RequestError:
        print("Request error")
        pass
    except sr.WaitTimeoutError:
        print("Say something?")
        pass
