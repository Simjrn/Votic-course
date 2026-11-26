import streamlit as st
from gtts import gTTS
import base64
import random

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay style="display:none;">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)
import streamlit as st
from gtts import gTTS
import io

with open("1/1.txt", encoding="utf-8") as f:
    split = f.read().splitlines()

# Render a single slider outside of any loop
num = st.slider("Go to question number ...", min_value=0, value=0, max_value=len(split) - 1)
current_line = split[num]

# Check if the line starts with + or -
if current_line.startswith(("+", "-")):
    index = current_line.find(":")
    # Safely extract text up to ':' (or the whole line if ':' isn't found)
    text_to_speak = current_line[1:index] if index != -1 else current_line[1:]
    
    if text_to_speak.strip():
        # Save audio to memory buffer instead of overwriting a local file
        audio_bytes = io.BytesIO()
        tts = gTTS(text=text_to_speak, lang="en", slow=False)
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        
        st.write(text_to_speak)
        autoplay_audio(audio_bytes)
else:
    st.write(current_line)

