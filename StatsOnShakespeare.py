# StatsOnShakespeare.py

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import networkx as nx

import seaborn as sns
import matplotlib.pyplot as plt 

import streamlit as st

# Dataset: https://www.kaggle.com/datasets/kingburrito666/shakespeare-plays?select=Shakespeare_data.csv

data = pd.read_csv('data/Shakespeare_data.csv', engine='python')
