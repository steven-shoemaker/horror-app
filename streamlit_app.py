import streamlit as st
import gpt_2_simple as gpt2
import pkg_resources
pkg_resources.require("tensorflow==1.15")
import tensorflow as tf

tf.reset_default_graph()


desc = "Uses a neural network trained on over *1000* horror movies to generate sometimes good, *mostly non-sensical* horror movie plots. "

st.title('Horror Movie Generator')

st.write(desc)
seed = st.text_input("")

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run1')



if st.button('Scare Me'):
    st.subheader("Your Terrible Movie:")
    generated_text = gpt2.generate(sess, length=50, temperature=0.7,  prefix=seed + " is", include_prefix = True, truncate='<|endoftext|>', return_as_list=True)[0]
    st.write(generated_text)