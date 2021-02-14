# load in the dependancies
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
import random


# image processing function
def create_training_data():
    
    # Use binary classes as labels of the directory
    for category in Classes:

        path = os.path.join(Datadirectory, category)
        class_num = Classes.index(category)

        # loop through each labeled directoryu
        for img in os.listdir(path):

            # Add images to training set
            try:
                img_path = os.path.join(path, img)
                img_array = cv2.imread(img_path)

                # normalize the image for optimal parsing
                img_size = 224
                new_array = cv2.resize(img_array, (img_size, img_size))
                training_Data.append([new_array, class_num])

            except Exception as e:
                # print('Failed to Grab Image')
                pass


# basic variables
img_size = 224
Datadirectory = 'Dataset/'
Classes = ['Louis', 'Not_Louis'] # i'm using class labels as the local directory names as-well

# training set
training_Data = []
create_training_data()
random.shuffle(training_Data)

X = [] # Features
y = [] # label

for features, label in training_Data:
    X.append(features)
    y.append(label)

# add image features to numpy matrix for max efficiency
X = np.array(X).reshape(-1, img_size, img_size, 3)
Y = np.array(y)
X = X/255

# load-in pre-trained keras model (lightweight image processing DL structure)
model = tf.keras.applications.mobilenet.MobileNet()

# extra junk needed to normalize the final layers of the model
base_input = model.layers[0].input
base_ouput = model.layers[-4].output
Flat_layer = layers.Flatten()(base_ouput)
final_output = layers.Dense(1)(Flat_layer)

# define binary classification nature
final_output = layers.Activation('sigmoid')(final_output)
new_model = keras.Model(inputs = base_input, outputs = final_output)
new_model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# fit the bad boy
new_model.fit(X, Y, epochs = 15, validation_split = 0.2)

# save the model
new_model.save('./Model/Fitted_Model.h5')
