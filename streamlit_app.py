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

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

local_css("style.css")
tokenizer = GPT2Tokenizer.from_pretrained("stevenshoemaker/horror")

model = AutoModelWithLMHead.from_pretrained("stevenshoemaker/horror")
device = torch.device("cpu")

model = model.to(device)

st.subheader("Enter the name of your film:")
model.eval()
prompt = st.text_input("") + " is about"

generated = torch.tensor(tokenizer.encode(prompt)).unsqueeze(0)
generated = generated.to(device)

if st.button('Scare Me'):
    sample_outputs = model.generate(
        generated,
         #bos_token_id=random.randint(1,30000),
         do_sample=True,
         top_k=40, 
         max_length = 300,
         top_p=0.98, 
        num_return_sequences=1,
                                )
    st.subheader(prompt[:-9])
    for i, sample_output in enumerate(sample_outputs):
            st.write("{}\n\n".format(tokenizer.decode(sample_output, skip_special_tokens=True)))