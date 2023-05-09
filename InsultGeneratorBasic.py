import random
import streamlit as st
import pandas as pd

file = "FILES/Shakespeare_Insults - insults.csv"
df = pd.read_csv(file)

col1, col2 = st.columns(2)
with col1:
  st.subheader("Bard's Insults")
  if st.button("Insults from Shakespeare's Plays"):
    rand_num = random.randint(1, (df.shape[0] - 1))

    st.write("Topic: ", str(df.iat[rand_num, 1]).upper())
    st.write("Line: ", df.iat[rand_num, 2])
    st.write("Act: ", df.iat[rand_num, 3])
    st.write("Scene: ", str(df.iat[rand_num, 4]))

with col2:
  st.subheader("Bot's Insults")
  insultAdverbs = "FILES/adverbList.txt"
  adverbs = pd.read_csv(insultAdverbs, sep = ' ')

  insultAdjectives = "FILES/adjectiveList.txt"
  adjectives = pd.read_csv(insultAdjectives, sep = ' ')

  insultNouns = "FILES/nounList.txt"
  nouns = pd.read_csv(insultNouns, sep = ' ')

  if st.button('Generate a Wacky Shakespeare-style Insult'):
    rand_num1 = random.randint(1, (adverbs.shape[0] - 1))
    rand_num2 = random.randint(1, (adjectives.shape[0] - 1))
    rand_num3 = random.randint(1, (nouns.shape[0] - 1))
    st.write("Thou ", str(adverbs.iat[rand_num1, 0]).lower(), str(adjectives.iat[rand_num2, 0]).lower(), str(nouns.iat[rand_num3, 0]).lower())
