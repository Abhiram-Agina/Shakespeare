
import random
import streamlit as st
import pandas as pd

st.write("Hello")

file = "Shakespeare_data.csv"
df = pd.read_csv(file)

if st.button('Random Player Line'):
  rand_num = random.randint(1,100000)
  st.write(df.iat[rand_num, 5])
