#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Written by: Vijay Sanjos Alexander
Email: vijaysanjosalexander@gmail.com
Copyright (c) 2017, VSA.
License: MIT (see LICENSE for details)
"""
import speech_recognition as sr
import pyttsx3
from time import ctime
import os

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        data = ""
        return data
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        data = r.recognize_sphinx(audio)
        return data
    return data

def speak(text):
    engine = pyttsx3.init()
    # Set the speed of speech
    engine.setProperty('rate', 115)
    # Male default voice
    engine.setProperty('voice', '0x000001F272AAFF28')
    engine.setProperty('volume', 10)
    engine.say(text)
    engine.runAndWait()


def MAX(data):

        if "hello" in data:
            speak("hello Angelina, how may I help you?")
            return
        if "how are you" in data:
            speak("I am fine")
            return
        if "what time is it" in data:
            speak(ctime())
            return
        if "where is" in data:
            data = data.split(" ")
            location = data[2]
            speak("Hold on Angelina, I will show you where " + location + " is.")
            os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
            return
        if "" in data:
            speak("I am sorry, could you please repeat")
            return


speak("Hi Angelina, am Max, what can I do for you?")
while 1:
    data = recordAudio()
    MAX(data)
