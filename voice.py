import streamlit as st
from gtts import gTTS
import os
import tempfile

# Streamlit App Title
st.title("🔊 Text-to-Speech Converter")
st.write("Enter text below, choose options, and download as MP3!")

# User Text Input
text = st.text_area("Enter Text:", "Hello! This is a text-to-speech app.")

# Language Selection
language_options = {"English": "en", "Urdu": "ur", "Hindi": "hi", "French": "fr"}
language = st.selectbox("Choose Language:", list(language_options.keys()))
language_code = language_options[language]

# Speak Button (gTTS)
if st.button("🔊 Speak"):
    tts = gTTS(text=text, lang=language_code, slow=False)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    
    # Play audio in Streamlit
    st.audio(temp_file.name, format="audio/mp3")
    st.success("Speaking... ✅")

# Generate and Download MP3 Button
if st.button("🎵 Download MP3"):
    tts = gTTS(text=text, lang=language_code, slow=False)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)

    # Provide Download Link
    with open(temp_file.name, "rb") as file:
        st.download_button("⬇️ Download Audio", file, file_name="speech.mp3", mime="audio/mp3")
    st.success("MP3 File Ready! ✅")
