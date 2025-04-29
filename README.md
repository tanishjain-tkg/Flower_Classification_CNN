# Flower Classification using CNN
This project implements a Convolutional Neural Network (CNN) to classify images of flowers into 5 distinct categories. Utilizing TensorFlow and Keras, the model is trained to recognize these 5 flower species- Daisy, Dandelion, Rose, Sunflower and Tulip.

## Project Structure
Flower_Classification_CNN/

├── Flower_Classification.ipynb      # Jupyter Notebook for model training and evaluation

├── Using_Model_To_Classify.py       # Script to load the trained model and classify new images

├── Flower_Class_Model.keras         # Saved Keras model

├── requirements.txt                 # List of required Python packages

├── sample/                          # Directory containing sample images

├── Images/                          # Directory containing training images

└── README.md                        # Project documentation

## Features
-Data Preprocessing: Efficient loading and preprocessing of image data using Keras utilities.

-Model Architecture: Custom CNN built with TensorFlow and Keras layers.

-Training & Evaluation: Model trained on a dataset of flower images with performance evaluation.

-Model Saving: Trained model saved in .keras format for future use.

-Image Classification: Script to classify new images using the trained model.

## Dataset
The famous kaggle flower dataset is used. The dataset contains nearly 4000 images of 5 flower species, organized into separate folders for each class. Ensure that the Images/ directory contains subdirectories for each flower category, each populated with corresponding images.

## Installation
For only using the model python environment should be setup on your systems as the requirements.txt only contains the modules specifically needed for this project.

### 1. Clone the Repository:

  git clone https://github.com/tanishjain-tkg/Flower_Classification_CNN.git
  
  cd Flower_Classification_CNN


### 2. Install Dependencies:

  pip install -r requirements.txt
  
  To access jupyter notebook file: setup jupyter environment on your system

## Usage

### 1. Train the Model

  Open the Jupyter Notebook:
  
  jupyter notebook Flower_Classification.ipynb
  
  Follow the instructions in the notebook to train and evaluate the model.

### 2. Classify New Images

  Use the provided script to classify new images using trained model:
  
  python Using_Model_To_Classify.py

## Reference
### 1. TensorFlow Official Tutorial – Image Classification

Link: https://www.tensorflow.org/tutorials/images/classification

Summary: This official guide walks through building a CNN model using TensorFlow and Keras to classify images of flowers. It includes data loading, augmentation, model building, training, and evaluation.

### 2. Keras Documentation – ImageDataGenerator and Preprocessing

Link: https://keras.io/api/preprocessing/image/

Summary: This page details how to load, augment, and preprocess images using Keras utilities like ImageDataGenerator, load_img, etc.—core tools used in your project.
