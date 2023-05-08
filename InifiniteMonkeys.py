# Infinite Monkey Theorem

# Shakespeare TEXT: https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt
# Inspiration: https://www.youtube.com/watch?v=3UWxIGk56C0&t=112s

import streamlit as st
import tensorflow as tf
import numpy as np
import os

# read the shakespeare works
path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
shakespeare = open(path_to_file, 'rb').read() #the entire corpus is now accessible via the variable named 'text'
shakespeare = shakespeare.decode(encoding='utf-8')
st.write('Total number of characters in the corpus is:', len(shakespeare)) # returns 178981 total characters
st.write('The first 500 characters of the corpus are as follows:\n', shakespeare[:500])

st.write("---")

# list of all characters in the book
typewriter = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ",", "!", "&", "?", "[", "]", " "]

# bestMatches stores the longest string of characters the monkey types that match shakepseare
bestMatches = [""]

# stores current string being typed by the monkey
currentRun = ""

# stores every single character the monkey typed
totalRun = ""

# total # of characters typed by the monkey
characterTotal = 0

import random

for x in range(0, 100000): #monkey types 100000 random characters; increase range as needed;
  newChar = random.choice(typewriter)
  currentRun += newChar
  totalRun += newChar
  characterTotal += 1

  if currentRun in shakespeare: # if our currentRun IS somewhere in shakespeare
    if len(currentRun) > len(bestMatches[0]): # if this is the longest match made so far, then reset the bestMatches to currentRun
      bestMatches = [currentRun]
      #st.write(bestMatches, "characters typed: {}".format(characterTotal))
    elif len(currentRun) == len(bestMatches[0]): # if this is the same length as the longest match made so far, then append the currentRun to bestMatches
      bestMatches.append(currentRun) 
      #st.write(bestMatches, "characters typed: {}".format(characterTotal))
  else:
    currentRun = "" # if our currentRun is NOT anywhere in shakespeare, then discard the currentRun and start over

# Once the above code run is complete, then print the bestMatches
st.write(bestMatches, "characters typed: {}".format(characterTotal))
#st.write("# words matched: ", len(bestMatches))
#st.write(" words matched: ", bestMatches)
