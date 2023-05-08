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
# st.write('Total number of characters in the corpus is:', len(text)) # returns 1115394
st.write('The first 100 characters of the corpus are as follows:\n', text[:100])

# Vectorize Text: STEP 1

# To give each unique character an index number, we first have to find all the unique characters in the text file. 
# This is very easy with the built-in set() function, which converts a list object to a set object.
# lists are ordered and allow duplicates, while sets are unordered and do not allow duplicates. Lists and Sets are data structures.

# The unique characters in the corpus
vocab = sorted(set(text)) #set(text) function returns a set of unique characters in the text file
#st.write('The number of unique characters in the corpus is', len(vocab)) # returns 65 unique characters i.e. 26 alphabets, 10 numbers, punctuation, and special characters.
#st.write('unique characters set:\n', vocab[:]) #prints all 65 unique characters 

# NOTE: in the above approach, RNN uses characters to generate new text. You could also create a vocab of unique words using the code below:
import re
words = re.findall('\w+', text.lower())
uniq_words = sorted(set(words)) #set() finds unique words; sorted() converts the set into a sorted array
len(uniq_words) #11,456 unique words
#st.write(uniq_words[:10]) # returns first 10 words from the 11,456 unique words

# Vectorize Text: STEP 2

# Create a mapping from unique characters to indices
char2idx = {u:i for i, u in enumerate(vocab)} # creates a dictionary of the set items with their index # to vectorize (encode the text)
# Make a copy of the unique set elements in NumPy array format for later use in the decoding the predictions
idx2char = np.array(vocab) #to de-vectorize (decode the text)
# Vectorize the text with a for loop
text_as_int = np.array([char2idx[c] for c in text]) # creates a vectorized numpy
