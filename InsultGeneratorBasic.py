
import random
import streamlit as st
import pandas as pd

file = "FILES/Shakespeare_Insults - insults.csv"
df = pd.read_csv(file)

if st.button('Generate an Insult'):
  rand_num = random.randint(1, (df.shape[0] - 1))
  
  st.write("Topic: ", str(df.iat[rand_num, 1]).upper())
  st.write("Line: ", df.iat[rand_num, 2])
  st.write("Act: ", df.iat[rand_num, 3], "\nScene: ", str(df.iat[rand_num, 4]))
