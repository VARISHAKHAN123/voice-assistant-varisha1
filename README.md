#  Voice Assistant – Built by Varisha Khanam

This project is my take-home assignment for EverythingAboutAI, where I’ve built a voice-powered assistant using Python. It can talk, understand commands, and perform real tasks like reminders, notes, and information lookup.

The main idea was to combine speech input/output with natural conversation using AI tools like Whisper, Wikipedia, and OpenAI GPT.

---

##  Technologies Used

- OpenAI Whisper (Speech-to-text)
-  pyttsx3 (Text-to-speech)
-  Wikipedia API (for general knowledge)
- ChatGPT (OpenAI GPT 3.5)
-  Python core: `threading`, `datetime`, `speech_recognition`, `sounddevice`

---

## What the Assistant Can Do

| Task                      | Voice Command Example                              |
|---------------------------|----------------------------------------------------|
|  Convert speech to text | "Tell me about AI" → Assistant understands it     |
|  Speak like a human     | Responds with natural voice (male/female voice)   |
|  Set reminders          | "Set a reminder for 10 seconds"                   |
|  Take notes             | "Take a note that I have a test tomorrow"         |
|  Search info (Wikipedia)| "Who is Abdul Kalam?" or "Tell me about Python"   |
|  GPT-based answers      | "Explain what is recursion"                       |
| Exit the assistant     | "Stop", "Exit", or "Quit"                         |

---

##  How to Set It Up (Step-by-Step)

1. **Install required libraries**:
   pip install openai-whisper pyttsx3 sounddevice scipy wikipedia openai
