import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)      # Speed of speech
    engine.setProperty("volume", 1.0)    # Volume (0.0 to 1.0)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)  # [0] = male, [1] = female
    engine.say(text)
    engine.runAndWait()

# Test it
speak("Hello Varisha! Your voice assistant is now speaking.")
