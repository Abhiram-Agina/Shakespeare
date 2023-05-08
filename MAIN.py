import streamlit as st
import pandas as pd
from PIL import Image

st.title('Bard vs Bot')
st.subheader("Shakespeare - Natural Language Processing")

# to get different images in the rows and columns, have a systematic way to label your images. For mine, I have used row_{i}_col_{j}

cols = st.columns(3)

cols[0].image('images/row_0_col_0.png', caption='Search Plays', use_column_width=True)
cols[2].markdown("[Search Shakespeare](https://abhiram-agina-shakespeare-filterworks-uzv0jn.streamlit.app/)")
cols[1].image('images/row_0_col_1.png', caption='Statistical Analysis', use_column_width=True)
cols[2].image('images/row_0_col_2.png', caption='Sentiment Analysis', use_column_width=True)

cols[0].image('images/row_1_col_0.png', caption='AI Play Writer', use_column_width=True)
cols[1].image('images/row_1_col_1.png', caption='Shakespeare', use_column_width=True)
cols[2].image('images/row_1_col_2.png', caption='Sonnet Clouds', use_column_width=True)
cols[2].markdown("[Sonnet Clouds](https://abhiram-agina-shakespeare-wordcloud-vbjvi0.streamlit.app/)")

cols[0].image('images/row_2_col_0.png', caption='Infinite MonkRandom', use_column_width=True)
cols[1].image('images/row_2_col_1.png', caption='Random Insults & Quotes', use_column_width=True)
cols[1].markdown("[Basic Insult Generator](https://abhiram-agina-shakespeare-insultgeneratorbasic-9povu7.streamlit.app/)")
cols[2].image('images/row_2_col_2.png', caption='Text Summary', use_column_width=True)
cols[2].markdown("[Text Summary](https://tulasi-agina-searchshakespeareplays-main-fpxl6w.streamlit.app/)")

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
