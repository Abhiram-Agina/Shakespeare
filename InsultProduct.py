import InsultBlueprint as insult
import streamlit as st

st.title("Shakespearean Insult Generator")

if st.button("Generate Insult"):
  st.write(insult.insult())
