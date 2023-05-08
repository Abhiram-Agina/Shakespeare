
import random
import streamlit as st
import pandas as pd

file = "FILES/Shakespeare_Insults - quotes.csv"
df = pd.read_csv(file)

st.title('Quotes from Shakespeare')
st.write('When you click on the button, a quote is randomly rendered, along with details like Play, Act & Scene.') 

if st.button('Generate a Quote'):
  rand_num = random.randint(1, (df.shape[0] - 1))
  
  st.write("Topic: ", str(df.iat[rand_num, 1]).upper())
  st.markdown(":blue[Line: ]", df.iat[rand_num, 2])
  st.write("Play: ", df.iat[rand_num, 3])
  st.write("Act: ", str(df.iat[rand_num, 4]))
  st.write("Scene: ", str(df.iat[rand_num, 5]))
