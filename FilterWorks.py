#Importing Libraries
import streamlit as st
import pandas as pd
import streamlit_pandas as sp

@st.cache_data
def load_data():
  df = pd.read_csv(file)
  return df

file = "Shakespeare_data.csv"
df = load_data()

#informs Streamlit on what values to allow as input
create_data = {"Dataline":"number",
                "Play": "multiselect",
               "PlayerLineNumber": "number",
               "ActSceneLine": "multiselect",
               "Player": "multiselect",
               "PlayerLine": "text"}

all_widgets = sp.create_widgets(df, create_data)
res = sp.filter_df(df, all_widgets)

st.title("Search Shakespeare")
st.header("Original Dataframe") #Prints raw dataframe
st.write(df)

st.header("Result Dataframe") #Prints filtered dataframe
st.write(res)

st.write('---')
st.video('https://www.youtu.be/QTu39aMg_mU') # Why you should read Hamlet?
