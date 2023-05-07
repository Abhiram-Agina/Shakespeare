
import random
import streamlit as st
import pandas as pd

file = "FILES/Shakespeare_Insults - insults.csv"
df = pd.read_csv(file)

if st.button('Generate an Insult'):
  rand_num = random.randint(1, (df.shape[0] - 1))
  
  st.write("Topic: ", df.iat[rand_num, 1])
  st.write("Line: ", df.iat[rand_num, 2])
  st.write("Act: ", df.iat[rand_num, 3], "Scene: ", str(df.iat[rand_num, 4]))
