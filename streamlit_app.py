import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AdamW, get_linear_schedule_with_warmup
import numpy as np
import os
import random
import streamlit as st
from transformers import AutoTokenizer, AutoModelWithLMHead

desc = "Uses a neural network trained on over *5000* horror movies to generate sometimes good, *mostly non-sensical* horror movie plots after being given a movie title. This program attempts it's best guess at generating a movie based on whatever title you give it. "

st.title('The Pitch Doctor')

st.write(desc)

import requests
import json
API_URL = "https://api-inference.huggingface.co/models/stevenshoemaker/horror"

if st.button('Scare Me'):
    payload = json.dumps(prompt)
    headers = {"Content-Type": "application/json", "Authorization": "Bearer <YOUR_API_KEY>"}
    response = requests.post(API_URL, payload, headers=headers)
    st.write(response.json())
    st.subheader(prompt[:-9]) )
