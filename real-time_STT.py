import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Say something in Arabic (MSA)...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    # Recognize speech using Google's Speech-to-Text API
    text = recognizer.recognize_google(audio, language="ar-SA") 
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError:
    print("Could not request results, check your internet connection.")

