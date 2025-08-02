import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt

# Load pre-trained InceptionV3 model (remove the final classification layer)
def load_model():
    base_model = InceptionV3(weights='imagenet')
    model = Model(inputs=base_model.input, outputs=base_model.layers[-2].output)
    return model

# Preprocess image (resize, normalize, reshape)
def preprocess_image(img_path):
    img = load_img(img_path, target_size=(299, 299))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

# Extract image features using the pre-trained model
def extract_features(model, img_path):
    processed_img = preprocess_image(img_path)
    features = model.predict(processed_img)
    return features

# Display image using matplotlib
def show_image(img_path):
    img = load_img(img_path)
    plt.imshow(img)
    plt.axis("off")
    plt.show()

# Main program
if __name__ == "__main__":
    image_path = "sample.jpg"  # Put your image file here
    model = load_model()
    features = extract_features(model, image_path)
    print("✅ Image features extracted successfully!")
    print("Feature shape:", features.shape)

    show_image(image_path)
