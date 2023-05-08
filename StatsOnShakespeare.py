# StatsOnShakespeare.py

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import networkx as nx

import seaborn as sns
import matplotlib.pyplot as plt 

import streamlit as st

# Dataset Source: https://www.kaggle.com/datasets/kingburrito666/shakespeare-plays?select=Shakespeare_data.csv
data = pd.read_csv('data/Shakespeare_data.csv', engine='python')

st.title("Statistical Analysis of the Works of Shakespeare")

add_selectbox = st.sidebar.selectbox(
    "Please select an analysis:",
    ("First 5", "Home phone", "Mobile phone"))

with 'First 5':
    st.write("first 5 records:")
    st.write(data.head(5))
