import speech_recognition as sr
from pydub import AudioSegment
import os

def convert_to_wav(audio_path):
    """Convert non-WAV audio files to WAV format"""
    if not audio_path.lower().endswith(".wav"):
        print("Converting audio to WAV format...")
        audio = AudioSegment.from_file(audio_path)
        new_path = audio_path.rsplit(".", 1)[0] + ".wav"
        audio.export(new_path, format="wav")
        return new_path
    return audio_path

def speech_to_text(audio_path):
    """Convert speech in an audio file to text using Google STT"""
    recognizer = sr.Recognizer()
    
    # Convert if not WAV
    wav_path = convert_to_wav(audio_path)

    with sr.AudioFile(wav_path) as source:
        print("Processing the audio file...")
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="ar-SA")  # Arabic (MSA)
        print("Recognized Text:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("API request failed, check your internet connection.")

    # Delete the converted WAV file if it was originally a different format
    if wav_path != audio_path:
        os.remove(wav_path)

# Example usage
audio_file = "sample_audio.wav"  #  (MP3, M4A, WAV, etc.)
speech_to_text(audio_file)
