# AI Playwright

# import libraries
import streamlit as st

# TensorFlow is an open source framework developed by Google researchers to run machine learning, deep learning and other statistical and predictive analytics workloads.
import tensorflow as tf
import numpy as np
import os

# load the dataset (i.e. shakespeare.txt) using the Keras API's util module in TensorFlow
path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

# Read the file, then decode for py2 compat.
text = open(path_to_file, 'rb').read() #the entire corpus is now accessible via the variable named 'text'
text = text.decode(encoding='utf-8')
st.write('Total number of characters in the corpus is:', len(text)) # returns 1115394
st.write('The first 100 characters of the corpus are as follows:\n', text[:100])
