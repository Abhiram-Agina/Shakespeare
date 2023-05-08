# TextSummarize.py
# Inspiration: Reference: https://www.activestate.com/blog/how-to-do-text-summarization-with-python/

import streamlit as st

'''
EXTRACTIVE SUMMARIZATION (as opposed to ABSTRACTIVE SUMMARIZATOIN): 
Rather than understanding the text, extractive summarization relies on quantitative metrics constructed from the text itself, 
without attaching any exogenous meaning. Our approach is to simply:
Look at the use frequency of specific words Sum the frequencies within each sentence Rank the sentences based on this sum Of course, 
our assumption is that a higher-frequency word use implies a more ‘significant’ meaning. 
This may seem overly simplistic, but this approach often produces surprisingly good results.
'''

import spacy # use SpaCy to import a pre-trained NLP pipeline to help interpret the grammatical structure of the text
from spacy.lang.en.stop_words import STOP_WORDS # to identify and filter out non-value adding words e.g., "the", "and", "between"
from string import punctuation # to identify and filter out punctuation, e.g., ",", "!"
from heapq import nlargest # to extract a percentage of the most important sentences

# Article to summarize

from newspaper import Article

url = 'https://www.sciencedaily.com/releases/2021/08/210811162816.htm'
article = Article(url)
article.download()
article.parse()

article.text #shows the first view lines of the article

'''
ALGORITHM:
Tokenize the text with the SpaCy pipeline. This segments the text into words, punctuation, and so on, using grammatical rules specific to the English language.
Count the number of times a word is used (not including stop words or punctuation), then normalize the count. A word that’s used more frequently has a higher normalized count.
Calculate the sum of the normalized count for each sentence.
Extract a percentage of the highest ranked sentences. These serve as our summary.
'''

def summarize(text, per): # NOTE: 'per' is the percentage (0 to 1) of sentences you want to extract
    nlp = spacy.load('en_core_web_sm') # 'en_core_web_sm' is the NLP dictionary for English (or the trained pipeline for English: https://spacy.io/models/en)
    doc= nlp(text)
    tokens=[token.text for token in doc] #tokenize the text
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS): # remove stopwords
            if word.text.lower() not in punctuation: # remove punctuation
                if word.text not in word_frequencies.keys(): # find word frequency
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents] #caculate the sum of counts for each sentence
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per) # extract the percentage of the highest ranked sentences
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    return summary
  
summarize(article.text, 0.05) #summarize to 0.05 i.e 5% of the original text
