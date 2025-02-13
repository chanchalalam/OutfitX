# -*- coding: utf-8 -*-

# packages in this training file

from training_module import *

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow import keras

from tensorflow.keras.preprocessing import image

from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
from tensorflow.keras.layers.experimental.preprocessing import StringLookup

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import cv2

import matplotlib.image as mpimg

# connect with google while working on colab
from google.colab import drive
drive.mount('/content/drive')



#use to unzip data

from zipfile import ZipFile
file_name = "archive.zip"

with ZipFile(file_name, 'r') as zip:
  zip.extractall()
  print('Done')


styles = get_df()

styles["subCategory"].unique() # we can check by this code that we only have three subcategory now.

"""# Model-1: """



le = LabelEncoder()
#
styles["subCategory"] = le.fit_transform(styles["subCategory"])




styles.head()

le.classes_



sub_train,sub_val,sub_test = make_input_xx(make_input_array_subcate(styles))

sub_model = build_model(80, 60)

sub_model.summary()

from tensorflow.keras.utils import plot_model
plot_model(sub_model)

sub_model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

sub_history = sub_model.fit(sub_train, 
                    epochs=5, 
                    steps_per_epoch = 2000,
                    validation_data = sub_val)

sub_model.save("/Users/chanchalalam/Desktop/Outfit_Recommendation_System-master/models/model_sub")

test_model = tf.keras.models.load_model("/Users/chanchalalam/Desktop/Outfit_Recommendation_System-master/models/model_sub")

test_model.evaluate(sub_test)

"""# Model 234"""


top_df = get_234_df("Topwear")
bottom_df = get_234_df("Bottomwear")
foot_df = get_234_df("Footwear")

top_df,top_art,top_gen,top_base,top_sea,top_usage = my_le(top_df)
bottom_df,bottom_art,bottom_gen,bottom_base,bottom_sea,bottom_usage = my_le(bottom_df)
foot_df,foot_art,foot_gen,foot_base,foot_sea,foot_usage = my_le(foot_df)

foot_usage.classes_

top_base_model = build_model(80,60,top_art,top_gen,top_base,top_sea,top_usage)
bottom_base_model = build_model(80,60,bottom_art,bottom_gen,bottom_base,bottom_sea,bottom_usage)
foot_base_model = build_model(80,60,foot_art,foot_gen,foot_base,foot_sea,foot_usage)


top_train, top_val, top_test = make_input_xx(make_input_array_2(top_df))
bottom_train, bottom_val, bottom_test = make_input_xx(make_input_array_2(bottom_df))
foot_train, foot_val, foot_test = make_input_xx(make_input_array_2(foot_df))

top_base_model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
bottom_base_model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
foot_base_model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

top_history = top_base_model.fit(top_train, 
                    epochs=10, 
                    steps_per_epoch = 500,
                    validation_data = top_val)

top_base_model.evaluate(top_test)

top_base_model.save("/Users/chanchalalam/Desktop/Outfit_Recommendation_System-master/models/model_top")



bottom_history = bottom_base_model.fit(bottom_train, 
                    epochs=15, 
                    steps_per_epoch = 50,
                    validation_data = bottom_val)

bottom_base_model.evaluate(bottom_test)

bottom_base_model.save("/Users/chanchalalam/Desktop/Outfit_Recommendation_System-master/models/model_bottom")



foot_history = foot_base_model.fit(foot_train, 
                    epochs=5, 
                    steps_per_epoch = 2000,
                    validation_data = foot_val)

foot_base_model.evaluate(foot_test)

foot_base_model.save("/Users/chanchalalam/Desktop/Outfit_Recommendation_System-master/models/model_shoes")

#!zip -r '"foot_model.zip"' '"foot_model"'


