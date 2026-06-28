"""
pip install tkinter: for U.I (built-In library)
pip install pyttsx3: for audio

pip install Speech_recognition: for speech to text
pip install pip PyAudio

"""

import tkinter # for ui
import pyttsx3 # for audio
import speech_recognition as Sr # for speech to text

engine = pyttsx3.init()
word = "Hello World"
engine.say(word)
engine.runAndWait()