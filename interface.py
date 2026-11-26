import streamlit as st
from gtts import gTTS
import base64
import random
import time
import io

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


st.markdown(
    """
    <style>
        div:has(> audio), audio {
            height: 0px !important;
            width: 0px !important;
            opacity: 0 !important;
            overflow: hidden !important;
            position: absolute !important;
            pointer-events: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with open("1/1.txt", encoding="utf-8") as f:
    split = f.read().splitlines()

num = st.slider("Go to question number ...", min_value=0, value=0, max_value=len(split) - 1)
current_line = split[num]

if current_line.startswith("-"):
    index = current_line.find(":")
    text_to_speak = f"What is '{current_line[1:index]}' in Votic?" if index != -1 else current_line[1:]
    
    if text_to_speak.strip():
        audio_bytes = io.BytesIO()
        tts = gTTS(text=text_to_speak, lang="en", slow=False)
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        
        st.header(text_to_speak)
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
        time.sleep(len(text_to_speak)/5)
        st.audio(f"1/{current_line[index+1:]}.mp3", format="audio/mp3", autoplay=True)
elif current_line.startswith("+"):
    index = current_line.find(":")
    text_to_speak = current_line[1:index] if index != -1 else current_line[1:]
    
    if text_to_speak.strip():
        audio_bytes = io.BytesIO()
        tts = gTTS(text=text_to_speak, lang="en", slow=False)
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
        st.write(text_to_speak)
        st.audio(f"1/{current_line[index+1:]}.mp3", format="audio/mp3", autoplay=True)
