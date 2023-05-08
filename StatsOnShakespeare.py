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
    
nav = st.sidebar.radio("Stats",["Summary", "Players", "Chart3", "Chart4", "Chart5"])
if nav == "Summary":
    st.write("first 5 records:")
    st.write(data.head(5))
    
    # Total number of Plays
    st.write("Number of plays are: " + str(data['Play'].nunique()))
    # List of Plays
    st.write(pd.DataFrame(data['Play'].unique().tolist(), columns=['Play Name']))

if nav == "Players":
    numberPlayers = data.groupby(['Play'])['Player'].nunique().sort_values(ascending= False).to_frame()
    numberPlayers['Play'] = numberPlayers.index.tolist()
    numberPlayers.columns = ['Num Players','Play']
    numberPlayers.index= np.arange(0,len(numberPlayers))
    numberPlayers

    plt.figure(figsize=(10,10))
    ax = sns.barplot(x='Num Players',y='Play',data=numberPlayers)
    ax.set(xlabel='Number of Players', ylabel='Play Name')
    st.pyplot()
