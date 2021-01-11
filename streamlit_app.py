import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AdamW, get_linear_schedule_with_warmup
import numpy as np
import os
import random
import streamlit as st
from transformers import AutoTokenizer, AutoModelWithLMHead


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

local_css("style.css")


desc = "Uses a neural network trained on over *5000* horror movies to generate sometimes good, *mostly non-sensical* horror movie plots after being given a movie title. This program attempts it's best guess at generating a movie based on whatever title you give it. "

st.title('The Pitch Doctor')

st.write(desc)


prompt = st.text_input("") + " is about"

import requests
import json
API_URL = "https://api-inference.huggingface.co/models/stevenshoemaker/horror"

if st.button('Scare Me'):
    payload = json.dumps(prompt)
    headers = {"Content-Type": "application/json", "Authorization": "Bearer <YOUR_API_KEY>"}
    response = requests.post(API_URL, payload, headers=headers)
    st.write(response.json())
    st.subheader(prompt[:-9]) 
