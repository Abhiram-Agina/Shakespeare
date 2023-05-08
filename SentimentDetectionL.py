import streamlit as st
import nltk
import tensorflow as tf
import textblob_download_utils
from textblob import TextBlob

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

st.title("Library-Based Sentiment Detection")

st.markdown("[Click here for Shakespeare Sonnets](https://nosweatshakespeare.com/sonnets/)")

sonnetInput = st.text_area("Paste a Shakespearean Sonnet or PlayerLine here to analyze the sentiment:", height=50) 

if st.button('Analyze Sentiment'):
  blob = TextBlob(sonnetInput)
  st.write('sentiment of the sonnet is:', blob.sentiment)

  if blob.sentiment.polarity < 0:
    st.write("negative sentiment")
  else:
    st.write("positive sentiment")

  if blob.sentiment.subjectivity < 0.5:
    st.write("objective")
  else:
    st.write("subjective")
  
#blob.words
