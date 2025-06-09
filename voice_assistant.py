import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.say("Setup is working, Varisha!")
engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand.")
