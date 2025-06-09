import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile
import pyttsx3
import time
import threading
from datetime import datetime
import wikipedia
import openai

# Load whisper model
model = whisper.load_model("base")

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # female voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def record_audio(duration=5):
    fs = 16000
    print(" Speak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print(" Recording complete.")
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, fs, audio)
        return f.name

def set_reminder(text):
    try:
        
        seconds = int([int(word) for word in text.split() if word.isdigit()][0])
        def remind():
            time.sleep(seconds)
            speak("⏰ Reminder! Time is up.")
        threading.Thread(target=remind).start()
        speak(f"Okay, I will remind you in {seconds} seconds.")
    except:
        speak("Sorry, I couldn't understand the time.")
        
#here i changed my api key for safety 

openai.api_key = "your api key"

def ask_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.7,
        )
        answer = response['choices'][0]['message']['content']
        return answer.strip()
    except Exception as e:
        return "Sorry, I couldn't process that right now."
     
        
        

def take_note(text):
    try:
    
        if "take a note" in text:
            note = text.replace("take a note", "").strip()
        elif "note that" in text:
            note = text.replace("note that", "").strip()
        else:
            note = text.strip()

        # Add timestamp
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        note_entry = f"[{now}] {note}\n"

        # Save  file
        with open("notes.txt", "a") as file:
            file.write(note_entry)

        speak("Your note has been saved.")
    except:
        speak("Sorry, I couldn't save the note.")

def search_info(query):
    try:
        topic = query.replace("who is", "").replace("tell me about", "").strip()
        result = wikipedia.summary(topic, sentences=2)
        print("📖 Info:", result)
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("That topic is too general. Please be more specific.")
    except:
        speak("Sorry, I couldn't find anything on that topic.")


def listen_and_respond():
    audio_path = record_audio()
    result = model.transcribe(audio_path)
    user_input = result["text"].lower()
    print("You said:", user_input)

    if "exit" in user_input or "stop" in user_input:
        speak("Okay, shutting down. Goodbye!")
        exit()

    elif "reminder" in user_input:
        set_reminder(user_input)

    elif "take a note" in user_input or "note that" in user_input:
        take_note(user_input)

    elif "who is" in user_input or "tell me about" in user_input:
        search_info(user_input)
        
    elif "chat" in user_input or "gpt" in user_input:
        query = user_input.replace("chat", "").replace("gpt", "").strip()
        ask_gpt(query)
    elif "what is" in user_input or "how does" in user_input:
        ask_gpt(user_input)
    else:
        response = ask_gpt(user_input)
        speak(response)



# Run continuously
while True:
    listen_and_respond()
