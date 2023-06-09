# -*- coding: utf-8 -*-
"""
Goal: Using RNN supplied with Shakespeare's Plays develop a Play.
"""

#Importing Libraries
import tensorflow as tf
import numpy as np
import os
import re

"""#### Loading Dataset & Reading """

#Loading Dataset
path_to_file = tf.keras.utils.get_file('ShakespearePlays.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

#Reading File
completeWorks = open(path_to_file, 'rb').read()
completeWorks = completeWorks.decode(encoding='utf-8')
print ('Total number of characters in the corpus is:', len(completeWorks)) # returns 1115394
print('The first 100 characters of the corpus are as follows:\n', completeWorks[:100])

#Vectorizing Text
vocab = sorted(set(completeWorks)) #set(text) function returns a set of unique characters in the text file
print ('The number of unique characters in the corpus is', len(vocab)) 
print('unique characters set:\n', vocab[:])


words = re.findall('\w+', completeWorks.lower())
uniq_words = sorted(set(words))
len(uniq_words)
print(uniq_words[:10])

char2idx = {u:i for i, u in enumerate(vocab)} 
idx2char = np.array(vocab)
text_as_int = np.array([char2idx[c] for c in completeWorks])


# Create training examples / targets
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
seq_length = 100 # The max. length for single input

sequences = char_dataset.batch(seq_length+1, drop_remainder=True) # returns <_BatchDataset element_spec=TensorSpec(shape=(101,), dtype=tf.int64, name=None)>

# for item in sequences.take(5): 
#   print(repr(''.join(idx2char[item.numpy()])))

def split_input_target(chunk):
  input_text = chunk[:-1]
  target_text = chunk[1:]
  return input_text, target_text

dataset = sequences.map(split_input_target)

# suffle the dataset and split it into 64 sentence batches

BUFFER_SIZE = 10000 # TF shuffles the data only within buffers
BATCH_SIZE = 64 # Batch size of 64 sentences each --> model accepts 64 input sentences at a time.
dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)
print(dataset) # returns <_BatchDataset element_spec=(TensorSpec(shape=(64, 100), dtype=tf.int64, name=None), TensorSpec(shape=(64, 100), dtype=tf.int64, name=None))>

# set parameters for the Model
# Length of the vocabulary in chars
vocab_size = len(vocab)
vocab_size # 64 unique characters

# The embedding dimension
embedding_dim = 256

# Number of RNN units
rnn_units = 1024

# Now, what is important about this is that our training pipeline will feed 64 sentences at each batch. 
# Therefore, we need to build our model to accept 64 input sentences at a time. 
# However, after we trained our model, we would like to input single sentences to generate new tasks. 
# So, we need different batch sizes for pre-training and post-training models. 
# To achieve this, we need to create a function, which allows us to reproduce models for different batch sizes. 

def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
  model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim,
                              batch_input_shape=[batch_size, None]),
    tf.keras.layers.GRU(rnn_units,
                        return_sequences=True,
                        stateful=True,
                        recurrent_initializer='glorot_uniform'),
    tf.keras.layers.Dense(vocab_size)
  ])
  return model

# create a model for training

model = build_model(
    vocab_size = len(vocab), # no. of unique characters
    embedding_dim=embedding_dim, # 256
    rnn_units=rnn_units, # 1024
    batch_size=BATCH_SIZE)  # 64 for the traning

model.summary()

# set our loss function and optimizer

def loss(labels, logits):
  return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

# example_batch_loss  = loss(target_example_batch, example_batch_predictions)
# print("Prediction shape: ", example_batch_predictions.shape, " (batch_size, sequence_length, vocab_size)")
# print("scalar_loss:      ", example_batch_loss.numpy().mean())

model.compile(optimizer='adam', loss=loss)

# To able to load our weights and save our training performance, we need to set and configure a checkpoint directory

# Directory where the checkpoints will be saved
checkpoint_dir = './training_checkpoints'
# Name of the checkpoint files
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)

# Our model and checkpoint directory are configured above.
# Now, we will train our model for 30 epochs and save the training history to a variable called history

EPOCHS = 30
history = model.fit(dataset, 
                    epochs=EPOCHS, 
                    callbacks=[checkpoint_callback])

"""#### Generating New Text"""

tf.train.latest_checkpoint(checkpoint_dir)

model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)
model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
model.build(tf.TensorShape([1, None]))
model.summary()

#Setting Up Model Input
def generate_text(model, num_generate, temperature, start_string):
  input_eval = [char2idx[s] for s in start_string] # string to numbers (vectorizing)
  input_eval = tf.expand_dims(input_eval, 0) # dimension expansion
  text_generated = [] # Empty string to store our results
  model.reset_states() # Clears the hidden states in the RNN

  for i in range(num_generate): #Run a loop for number of characters to generate
    predictions = model(input_eval) # prediction for single character
    predictions = tf.squeeze(predictions, 0) # remove the batch dimension

    # using a categorical distribution to predict the character returned by the model
    # higher temperature increases the probability of selecting a less likely character
    # lower --> more predictable
    predictions = predictions / temperature
    predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

    # The predicted character as the next input to the model
    # along with the previous hidden state
    # So the model makes the next prediction based on the previous character
    input_eval = tf.expand_dims([predicted_id], 0) 
    # Also devectorize the number and add to the generated text
    text_generated.append(idx2char[predicted_id]) 

  return (start_string + ''.join(text_generated)) # returns our final prediction value

st.title("Generating Shakespearean Plays")

startingString = st.text_area('Enter an intriductory statement for me to build off of:')
generated_text = generate_text(
                    model, 
                    num_generate=500, 
                    temperature=1, 
                    start_string = startingString)

st.header("Resulting Text")
st.write(generated_text)
