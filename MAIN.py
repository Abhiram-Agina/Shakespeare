import streamlit as st
import pandas as pd
from PIL import Image

st.title("**Shakespeare - Natural Language Processing**")

shakespearePortraitPic = Image.open("IMAGES/ShakespearePortrait.jpeg")
st.image(shakespearePortraitPic, width = 300)

st.header("*Apps*")
st.markdown(
'''
* [Word Cloud Generator](https://abhiram-agina-shakespeare-wordcloud-vbjvi0.streamlit.app/)
* [Filtering Shakespeare](https://abhiram-agina-shakespeare-filterworks-uzv0jn.streamlit.app/)
* [Sentiment Detection](https://abhiram-agina-shakespeare-sentimentdetectionl-dt0usp.streamlit.app/)
'''
)
