import streamlit as st

view = st.empty()
screen = view.container()

with open ("1/1.txt", encoding='utf-8') as f:
  f = f.read()
  split = f.splitlines()
  slide = 0
  for line in split:
    num = screen.slider("Go to question number ...", min_value=0, value=slide, max_value=len(split))
    st.write(split[num])    
