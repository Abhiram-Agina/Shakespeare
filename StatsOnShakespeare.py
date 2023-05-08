# StatsOnShakespeare.py

import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud, STOPWORDS
import glob, nltk, os, re
from nltk.corpus import stopwords 
import nltk
nltk.download('punkt')
import string
nltk.download('stopwords')
