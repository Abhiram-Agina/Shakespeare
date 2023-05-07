import streamlit as st
import pandas as pd
from PIL import Image

st.title(Bard v Bot)
st.header("**Shakespeare - Natural Language Processing**")

shakespearePortraitPic = Image.open("IMAGES/ShakespearePortrait.jpeg")
st.image(shakespearePortraitPic, width = 300)

st.header("*Apps*")
st.markdown(
'''
* [Word Cloud Generator](https://abhiram-agina-shakespeare-wordcloud-vbjvi0.streamlit.app/)
* [Filtering Shakespeare](https://abhiram-agina-shakespeare-filterworks-uzv0jn.streamlit.app/)
* [Sentiment Detection](https://abhiram-agina-shakespeare-sentimentdetectionl-dt0usp.streamlit.app/)
* [Basic Insult Generator](https://abhiram-agina-shakespeare-insultgeneratorbasic-9povu7.streamlit.app/)
* [Basic Quote Generator](https://abhiram-agina-shakespeare-quotegeneratorbasic-ltfk2v.streamlit.app/)
* [Wacky Insult Generator](https://abhiram-agina-shakespeare-randomizedinsults-hfug85.streamlit.app/)
'''
)
