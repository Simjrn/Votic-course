import streamlit as st
from gtts import gTTS

audios = []
with open("1/1.txt") as lesson:
  for line in lesson:
    if line.startswith("+"):
      myobj = gTTS(text=line[1:], lang="en", slow=False)
      myobj.save(f"1/{line[1:]}.mp3")
