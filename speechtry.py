# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 03:24:12 2022

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

dictation_modeon= 0
navigation_modeon=0
def dictation_navigator(command):
    if "up" in command:
        print("^\n"*4)
    elif "down" in command:
        print("v\n"*4)
    elif "next line" in command or '9' in command:
        print("\n")
    elif "right" in command or "write" in command:
        print(">"*4)
    elif "left" in command:
        print("<"*4)
    else:
        print("hmm")
        
        
def set_reminder(command):
       return


def listening(source):
     print('Adjusting...')
     listener.adjust_for_ambient_noise(source, duration=3)
     print('Listening...')
     voice = listener.listen(source, phrase_time_limit=20)
     print("Recognizing...")
     return listener.recognize_google(voice)
     
while(1):
    try:
        with sr.Microphone(device_index=1) as source:
           
            
            command = listening(source)
            command = command.lower()
            print(command)
            if 'dictate' in command: #speak this
                dictation_modeon= 1
                speak("Starting dictation mode. Say 'exit' to stop.")
            if 'exit' in command:
                speak("Quitting mode")
                break
            if dictation_modeon == 1:
                if navigation_modeon == 0:
                    speak("Do you wish to navigate?")
                command = listening(source)
                print(command)
                if "yes" in command:
                    navigation_modeon = 1
                    speak("Starting navigation mode. Options available are; 'go up', 'go down', 'go right', 'go left' and 'next line'. Say 'exit' to stop.")
                    while command != "exit":
                        command = listening(source)
                        print(command)
                        dictation_navigator(command)
    except sr.UnknownValueError:
        print("Unknown value!")        
        pass
    except sr.RequestError:
        print("Request error")
        pass
    except sr.WaitTimeoutError:
        print("Say something?")
        pass

