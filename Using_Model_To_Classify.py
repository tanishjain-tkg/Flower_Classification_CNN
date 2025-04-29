import os
import keras
from keras.models import load_model
import streamlit as st 
import tensorflow as tf
import numpy as np
from tkinter import Tk, filedialog

model = load_model('Flower_Class_Model.keras')
flower_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

def classify_images(image_path):
    input_image = tf.keras.utils.load_img(image_path, target_size=(180,180))
    input_image_array = tf.keras.utils.img_to_array(input_image)
    input_image_exp_dim = tf.expand_dims(input_image_array,0)

    predictions = model.predict(input_image_exp_dim)
    result = tf.nn.softmax(predictions[0])
    outcome = 'The Image belongs to ' + flower_names[np.argmax(result)] + ' with a score of '+ str(np.max(result)*100)
    return outcome

file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")]
)
print(classify_images(file_path))