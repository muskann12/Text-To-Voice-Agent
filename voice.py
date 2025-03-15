import streamlit as st
import pyttsx3
from gtts import gTTS
import os


st.title("🔊 Text-to-Speech Converter")
st.write("Enter text below, choose options, and download as MP3!")

# User Text Input
text = st.text_area("Enter Text:", "Hello! This is a text-to-speech app.")

# Voice Selection
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_option = st.radio("Select Voice:", ["Male", "Female"])

# Set voice properties
if voice_option == "Male":
    engine.setProperty('voice', voices[0].id)
else:
    engine.setProperty('voice', voices[1].id)

# Speed Control
rate = st.slider("Speech Speed:", 100, 300, 150)
engine.setProperty('rate', rate)

# Language Selection
language_options = {"English": "en", "Urdu": "ur", "Hindi": "hi", "French": "fr"}
language = st.selectbox("Choose Language:", list(language_options.keys()))
language_code = language_options[language]

# Speak Button
if st.button("🔊 Speak"):
    engine.say(text)
    engine.runAndWait()
    st.success("Speaking... ✅")

# Generate and Download MP3 Button
if st.button("🎵 Download MP3"):
    tts = gTTS(text=text, lang=language_code, slow=False)
    tts.save("speech.mp3")
    st.success("MP3 File Ready! ✅")
    
    #  Download Link
    with open("speech.mp3", "rb") as file:
        st.download_button("⬇️ Download Audio", file, file_name="speech.mp3", mime="audio/mp3")
