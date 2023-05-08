# Infinite Monkey Theorem

# Romeo and Juliet TEXT: https://github.com/cgovella/learning/blob/master/edx-python/case%20studies/gutenverg/Books/English/shakespeare/Romeo%20and%20Juliet.txt
# Inspiration: https://www.youtube.com/watch?v=3UWxIGk56C0&t=112s

import tensorflow as tf
import numpy as np
import os

# read the shakespeare works
path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
shakespeare = open(path_to_file, 'rb').read() #the entire corpus is now accessible via the variable named 'text'
shakespeare = shakespeare.decode(encoding='utf-8')
st.write('Total number of characters in the corpus is:', len(shakespeare)) # returns 178981 total characters
st.write('The first 500 characters of the corpus are as follows:\n', shakespeare[:500])
