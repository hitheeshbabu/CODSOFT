import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Dummy word-index dictionary
word_to_index = {'start': 1, 'a': 2, 'cat': 3, 'on': 4, 'mat': 5, 'end': 6}
index_to_word = {v: k for k, v in word_to_index.items()}
vocab_size = len(word_to_index) + 1  # +1 for padding

# Dummy feature (replace this with your real extracted features)
dummy_feature = np.random.rand(1, 2048)

# Dummy caption sequence (for simulation)
input_sequence = [1, 2, 3, 4, 5, 6]  # 'start a cat on mat end'

# Model definition
def create_caption_model():
    model = Sequential()
    model.add(Embedding(input_dim=vocab_size, output_dim=10, input_length=5))
    model.add(LSTM(256))
    model.add(Dense(vocab_size, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model

# Simulate caption prediction
def generate_caption():
    print("🧠 Simulated caption:")
    print("start a cat on mat end")

# Main program
if __name__ == "__main__":
    model = create_caption_model()
    generate_caption()
