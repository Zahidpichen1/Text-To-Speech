import os
from gtts import gTTS
import streamlit as st
prompt = st.text_area("Enter your message", max_chars=2000)
if prompt:
    display = st.write(prompt)
    voice_apply = st.button("Apply Voice")
    if voice_apply: 
        language = 'en'
        voice = gTTS(text=prompt, lang=language, slow=False)  # Use prompt directly, not prompt_text
        voice.save("voice.mp3")
        audio_file = open('voice.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')  # Display the audio
