import streamlit as st
from gtts import gTTS
import base64

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


audio = gTTS(text="hello", lang="en", slow=False)
audio.save("audio.mp3")
autoplay_audio("audio.mp3")


view = st.empty()
screen = view.container()

with open ("1/1.txt", encoding='utf-8') as f:
  f = f.read()
  split = f.splitlines()
  slide = 0
  for line in split:
    num = screen.slider("Go to question number ...", min_value=0, value=slide, max_value=len(split)-1)
    if split[num].startswith("+"):
      index = split[num].find(":")
      audio = gTTS(text=split[num][1:index], lang="en", slow=False)
      audio.save("audio.mp3")
      autoplay_audio("audio.mp3")
    if split[num].startswith("-"):
      index = split[num].find(":")
      audio = gTTS(text=split[num][1:index], lang="en", slow=False)
      audio.save("audio.mp3")
      autoplay_audio("audio.mp3")
