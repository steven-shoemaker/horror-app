import streamlit as st
import gpt_2_simple as gpt2
import pkg_resources
pkg_resources.require("tensorflow==1.15")
import tensorflow as tf

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run1')

