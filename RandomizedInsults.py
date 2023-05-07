import random
import streamlit as st
import pandas as pd

insultAdverbs = "FILES/adverbList.txt"
adverbs = pd.read_csv(insultAdverbs, sep = ' ')

insultAdjectives = "FILES/adjectiveList.txt"
adjectives = pd.read_csv(insultAdjectives, sep = ' ')

insultNouns = "FILES/nounList.txt"
nouns = pd.read_csv(insultNouns, sep = ' ')


if st.button('Generate a Wacky Shakespearean Insult'):
  rand_num1 = random.randint(1, (adverbs.shape[0] - 1))
  rand_num2 = random.randint(1, (adjectives.shape[0] - 1))
  rand_num3 = random.randint(1, (nouns.shape[0] - 1))
  st.write("Thou ", str(adverbs.iat[rand_num, 0]).upper(), str(adjectives.iat[rand_num, 0]).upper(), str(nouns.iat[rand_num, 0]).upper())
