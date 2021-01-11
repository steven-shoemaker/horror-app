import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

local_css("style.css")


desc = "Uses a neural network trained on over *5000* horror movies to generate sometimes good, *mostly non-sensical* horror movie plots after being given a movie title. This program attempts it's best guess at generating a movie based on whatever title you give it. "

st.title('The Pitch Doctor')

st.write(desc)

st.subheader("Enter the name of your film:")
prompt = st.text_input("") + " is a movie about"

import requests
import json
import time
API_URL = "https://api-inference.huggingface.co/models/stevenshoemaker/horror"

if st.button('Scare Me'):
    payload = json.dumps(prompt)
    headers = {"Content-Type": "application/json", "Authorization": "Bearer <YOUR_API_KEY>"}
    response = requests.post(API_URL, payload, headers=headers)
    time.sleep(1)
    st.subheader(prompt[:-17]) 
    st.write(response.json()[0]["generated_text"])
  
