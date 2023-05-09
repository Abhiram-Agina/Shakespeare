import streamlit as st
import nltk
import tensorflow as tf
import textblob_download_utils
from textblob import TextBlob

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

st.title("Library-Based Sentiment Detection")

st.markdown("[Click here for Shakespeare Sonnets](https://nosweatshakespeare.com/sonnets/)")
st.markdown("[Or have Captain Kirk read them to you](https://www.youtube.com/hashtag/asonnetaday)")
sonnetInput = st.text_area("Paste a Shakespearean Sonnet or PlayerLine here to analyze the sentiment:", height=300) 

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
st.write('---')
st.video('https://www.youtu.be/ZNMwhaSHK9Q') # Shakesearean Dating Tips
