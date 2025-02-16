import streamlit as st
import speech_recognition as sr

# Function for real-time speech recognition
def record_and_recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio, language="ar-SA")  # Arabic (MSA)
        return text
    except sr.UnknownValueError:
        return "Sorry, could not understand the speech."
    except sr.RequestError:
        return "API request failed, check your internet connection."

# Streamlit UI
st.title("🎙️ Real-Time Speech-to-Text (STT) for Arabic (MSA)")
st.write("Click the **Start Listening** button and speak.")

# Start recognition when button is clicked
if st.button("Start Listening 🎙️"):
    text = record_and_recognize()
    st.success(f"Recognized Text: {text}")
