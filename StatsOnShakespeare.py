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

st.set_option('deprecation.showPyplotGlobalUse', False)

st.subheader("Statistical Analysis of the Works of Shakespeare")
    
nav = st.sidebar.radio("Stats",["Summary", "Players", "Lines", "Play", "Emotion"])
if nav == "Summary":
    st.write("First 5 records of the Shakespeare Corpus:")
    st.write(data.head(5))
    
    # Total number of Plays
    # st.write("Number of plays are: " + str(data['Play'].nunique()))
    # List of Plays
    # st.write(pd.DataFrame(data['Play'].unique().tolist(), columns=['Play Name']))

if nav == "Players": # Players per Play
    st.write("Number of Players per Play")
    numberPlayers = data.groupby(['Play'])['Player'].nunique().sort_values(ascending= False).to_frame()
    numberPlayers['Play'] = numberPlayers.index.tolist()
    numberPlayers.columns = ['Num Players','Play']
    numberPlayers.index= np.arange(0,len(numberPlayers))
    #numberPlayers

    plt.figure(figsize=(10,10))
    ax = sns.barplot(x='Num Players',y='Play',data=numberPlayers)
    ax.set(xlabel='Number of Players', ylabel='Play Name')
    st.pyplot()

if nav == "Lines": # PlayerLines per Play
    st.write(" Number of PlayerLines per Play")
    plt.rcParams['figure.figsize']=(12.5,5)
    ax= sns.barplot(x='Play',y='PlayerLinenumber',data=data)
    plt.setp(ax.get_xticklabels(), rotation=90)
    st.pyplot()

if nav == "Play": # Lines per Player in a given Play
    # Lines per Player in a given Play
    # Players who dominate the stage (based on #lines spoken)
    st.write('Number of Lines per Player in a given Play')
    play = st.selectbox('Please select a play', data['Play'].unique())
    
    # play = "Alls well that ends well" # NOTE: Change this Play name to get the #Lines per Player for that Play
    p_line = data[data['Play']==play].groupby('Player').count().sort_values(by='PlayerLine',ascending=False)['PlayerLine']
    p_line = p_line.to_frame()
    p_line['Player'] = p_line.index.tolist()
    p_line.index = np.arange(0,len(p_line))
    p_line.columns=['Lines','Player']

    plt.figure(figsize=(10,10))
    ax = sns.barplot(x='Lines',y='Player',data=p_line)
    ax.set(title=play, xlabel='Number of Lines', ylabel='Player')
    st.pyplot()

if nav == "Emotion": # Lines per Player in a given Play
    # Lines per Player in a given Play
    # Players who dominate the stage (based on #lines spoken)
    
    play = st.selectbox('Please select a play', data['Play'].unique())
    emote = st.text_input('Please type an emotion/keyword to search. For example: life')
    #emote = st.selectbox('Please select an emotion to search', ("Love", "Murder", "Alas", "Marry"))
    st.write('Note: currently, this searches for the keyword - I will expand this to search for emotions')
    emote = emote.lower()
    # play = "Alls well that ends well" # NOTE: Change this Play name to get the #Lines per Player for that Play
    data = data[data['PlayerLine'].str.contains(emote)]
    p_line = data[data['Play']==play].groupby('Player').count().sort_values(by='PlayerLine',ascending=False)['PlayerLine']
    p_line = p_line.to_frame()
    p_line['Player'] = p_line.index.tolist()
    p_line.index = np.arange(0,len(p_line))
    p_line.columns=['Lines','Player']

    plt.figure(figsize=(10,10))
    ax = sns.barplot(x='Lines',y='Player',data=p_line)
    ax.set(title=play, xlabel='Number of Lines', ylabel='Player')
    st.pyplot()
    
st.write('---')
st.video('https://www.youtu.be/lv4fWhObaTM') # New York Times: There's no escaping Shakespeare


st.write("""
**Project Description:**\n
This program conducts statistical analysis of Shakespeare's Complete Works.\n
Program #1 graphs the number of appearing characters per play.\n
Program #2 graphs the average number of lines per character per play.\n
Program #3 graphs the number of lines for each character in a selected play.\n
Program #4 graphs the frequency of a given theme as stated by each player.\n
""")
