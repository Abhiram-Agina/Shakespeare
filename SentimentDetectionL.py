import streamlit as st
import nltk
import tensorflow as tf
import textblob_download_utils
from textblob import TextBlob

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

st.title("Library-Based Sentiment Detection")

st.markdown("[Click here for Shakespeare Speeches](https://nosweatshakespeare.com/quotes/monologues/)")

sonnetInput = st.text_area("Paste a Shakespearean Sonnet or Speech here to analyze the sentiment:", '''
To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die—to sleep,
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to: 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep, perchance to dream—ay, there's the rub:
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause—there's the respect
That makes calamity of so long life.
For who would bear the whips and scorns of time,
Th'oppressor's wrong, the proud man's contumely,
The pangs of dispriz'd love, the law's delay,
The insolence of office, and the spurns
That patient merit of th'unworthy takes,
When he himself might his quietus make
With a bare bodkin? Who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscovere'd country, from whose bourn
No traveller returns, puzzles the will,
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience doth make cowards of us all,
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry
And lose the name of action.''',
height=800) 

if st.button('Analyze Sentiment'):
  blob = TextBlob(sonnetInput)
  st.write('sentiment of the sonnet is:', blob.sentiment)

  if blob.sentiment.polarity < 0:
    st.write("negative sentiment")
  else:
    st.write("positive sentiment")

  if blob.sentiment.subjectivity < 0.5:
    st.write("objective")
  else:
    st.write("subjective")
  
#blob.words
st.write('---')
st.video('https://www.youtu.be/ZNMwhaSHK9Q') # Shakesearean Dating Tips

st.write("""
  **Project Description:**\n
  This program identifies the underlying emotion in a passage.\n  
  The program works by breaking apart (tokenizing) the text and evaluating deeper meaning through matching words to their synonyms.\n
""")
