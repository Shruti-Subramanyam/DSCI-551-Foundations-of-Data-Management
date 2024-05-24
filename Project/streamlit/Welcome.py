import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
logo = Image.open("logo.png")
vege = Image.open("vegepic.jpg")

col1_width = 1
col2_width = 8

col1, col2 = st.columns([col1_width, col2_width])
with col1:
    st.image(logo, use_column_width=True)

with col2:
    st.write('# Welcome to the Exchange Market👋')

st.markdown('**👈 Select a page from the sidebar**')
st.image(vege, use_column_width=True)
