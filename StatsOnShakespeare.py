# StatsOnShakespeare.py

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import networkx as nx

import seaborn as sns
import matplotlib.pyplot as plt 

import streamlit as st

# Dataset Source: https://www.kaggle.com/datasets/kingburrito666/shakespeare-plays?select=Shakespeare_data.csv
data = pd.read_csv('data/Shakespeare_data.csv', engine='python')

# replace 'NaN' with 'Other' in the Player column
data['Player'].replace(np.nan, 'Other',inplace = True)

st.title("Statistical Analysis of the Works of Shakespeare")
    
nav = st.sidebar.radio("Stats",["First 5 Rows", "Chart2", "Chart3", "Chart4", "Chart5"])
if nav == "First 5 Rows":
    st.write("first 5 records:")
    st.write(data.head(5))
