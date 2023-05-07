import streamlit as st
import nltk
import tensorflow as tf

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

st.title("Library-Based Sentiment Detection")

sonnetInput = st.text_area("Paste Shakespearean Sonnet Here:") 

from textblob import TextBlob

blob = TextBlob(sonnetInput)
print('sentiment of the sonnet is:', sonnetInput.sentiment)

if blob.sentiment.polarity < 0:
  print("negative sentiment")
else:
  print("positive sentiment")

if blob.sentiment.subjectivity < 0.5:
  print("objective")
else:
  print("subjective")
  
#blob.words
