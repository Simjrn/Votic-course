import streamlit as st
from gtts import gTTS

with open("1/1.txt") as lesson:
  for line in lesson:
    if line.startswith("+"):
      myobj = gTTS(text=line[1:, lang="en", slow=False)
