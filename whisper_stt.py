import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile

# Load Whisper model (base/light/small for speed)
model = whisper.load_model("base")

# Record voice
def record_audio(duration=5):
    print("🎤 Speak now...")
    fs = 16000
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("✅ Recording done.")

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, fs, audio)
        return f.name

# Transcribe audio
def transcribe():
    audio_path = record_audio()
    result = model.transcribe(audio_path)
    print("📝 You said:", result["text"])


transcribe()
