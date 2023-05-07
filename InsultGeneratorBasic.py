
import random
import streamlit as st
import pandas as pd

st.write("Hello")

file = "FILES/Shakespeare_Insults - insults.csv"
df = pd.read_csv(file)

if st.button('Random Player Line'):
  rand_num = random.randint(1, df.shape[0])
  st.write(df.iat[rand_num, 5])
