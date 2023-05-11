import streamtlit as st

import pandas as pd
import matplotlib.pyplot as plt

#Inputting Text
textInput = """Not marble, nor the gilded monuments
Of princes, shall outlive this powerful rhyme;
But you shall shine more bright in these contents
Than unswept stone, besmear’d with sluttish time.
When wasteful war shall statues overturn,
And broils root out the work of masonry,
Nor Mars his sword, nor war’s quick fire shall burn
The living record of your memory.
‘Gainst death, and all oblivious enmity
Shall you pace forth; your praise shall still find room
Even in the eyes of all posterity
That wear this world out to the ending doom.
So, till the judgment that yourself arise,
You live in this, and dwell in lovers’ eyes."""

#Defining Parameters
letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Splitting Input
tokenizedInput = (textInput.lower()).split()
print(tokenizedInput)

#Counting Letters - TOTAL
letterCounts = []
counter = 0

for match in letterList:
  counter = 0
  for token in tokenizedInput:
    for letter in token:
      if match == letter:
        counter = counter + 1
  letterCounts.append(counter)

#print(letterList)
#print(letterCounts)

#Crafting Graph - TOTAL
plt.bar(letterList, letterCounts)
plt.title('Most Used Letters - TOTAL')
plt.xlabel('Letter')
plt.ylabel('Frequency')
plt.show()

#Counting Letters - START
startCounts = []
counter = 0

for match in letterList:
  counter = 0
  for token in tokenizedInput:
    if match == token[0]:
      counter = counter + 1
  startCounts.append(counter)

#print(letterList)
print(startCounts)

#Crafting Graph - START
plt.bar(letterList, startCounts)
plt.title('Most Used Letters - Starting')
plt.xlabel('Letter')
plt.ylabel('Frequency')
plt.show()
