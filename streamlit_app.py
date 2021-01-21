import streamlit as st
from nltk.tokenize import sent_tokenize 

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

local_css("style.css")


desc = "Uses a neural network trained on over *5000* horror movies to generate sometimes good, *mostly non-sensical* horror movie plots after being given a movie title. This program attempts it's best guess at generating a movie based on whatever title you give it. "
st.title('The Pitch Doctor')
st.markdown("<b>Note, this app is still in-development so you may receive cut off responses or other errors. Please be kind!</b>", unsafe_allow_html=True)
st.write("Created by: [Steven Shoemaker](https://twitter.com/_stevenshoe)")
st.write(desc)

st.subheader("Enter the name of your film and hit enter:")
prompt = st.text_input("") + " is about"

import requests
import json
import time
import re
payload = json.dumps(prompt)

from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
punkt_param = PunktParameters()
punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc'])
sentence_splitter = PunktSentenceTokenizer(punkt_param)


API_URL = "https://api-inference.huggingface.co/models/stevenshoemaker/horror"

if st.button('Scare Me'):
     try:
          time.sleep(1)
          headers = {"Content-Type": "application/json", "Authorization": "Bearer <YOUR_API_KEY>"}
          response = requests.post(API_URL, payload, headers=headers)
          movie = response.json()[0]["generated_text"]
          st.subheader(prompt[:-8]) 
          movie = sentence_splitter.tokenize(movie)[:-1]
          st.markdown(' '.join(word for word in movie))
     except: 
         st.write("Our servers are dusting off some cobwebs, can you please try your response again or use a different movie name?")
  
