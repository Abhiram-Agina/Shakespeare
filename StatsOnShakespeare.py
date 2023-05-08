# StatsOnShakespeare.py

import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud, STOPWORDS
import glob, nltk, os, re
from nltk.corpus import stopwords 
import nltk
nltk.download('punkt')
import string
nltk.download('stopwords')

# Create a dictionary (not a list)
books = {" ":" ","A Mid Summer Night's Dream":"data/summer.txt","The Merchant of Venice":"data/merchant.txt","Romeo and Juliet":"data/romeo.txt"}

## Select text files
pickPlay = st.selectbox("Choose a text file", books.keys())

## Get the value
pickPlay = books.get(pickPlay)
tab1, tab2, tab3 = st.tabs(['Word Cloud', 'Bar Chart', 'View Text'])

if pickPlay != " ":
    stop_words = []
    raw_text = open(pickPlay,"r").read().lower()
    nltk_stop_words = stopwords.words('english')
    
    stop_words = set(nltk_stop_words)
    tokens = nltk.word_tokenize(raw_text)
    
    st.write(pickPlay)
