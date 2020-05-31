from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import os
import cv2
import tensorflow as tf
import keras
from keras.models import Model
from keras.layers import *
from keras.optimizers import *
from scse import channel_spatial_squeeze_excite
from keras.callbacks import *
from keras.utils.np_utils import to_categorical

def create_model(inputs_):
  o = Conv2D(32, (3, 3), padding='same', kernel_initializer='random_uniform')(inputs_)
  o = channel_spatial_squeeze_excite(o)
  o = MaxPooling2D((2, 2))(o)
  o = Conv2D(64, (3, 3), padding='same', kernel_initializer='random_uniform')(o)
  o = channel_spatial_squeeze_excite(o)
  o = MaxPooling2D((2, 2))(o)
  o = Conv2D(64, (3, 3), padding='same', kernel_initializer='random_uniform')(o)
  o = channel_spatial_squeeze_excite(o)
  #x = Dense(64, activation='relu')(x)
  o = Flatten()(o)
  o = Dense(6, activation='softmax')(o)
  model = Model(inputs=inputs_, outputs=o)
  model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
  return model


def make_train_dataset(img_dir):
    x = []
    y =[]
    label = 0
    for c in os.listdir(img_dir):
        print('class: {}, class id: {}'.format(c, label))
        d = os.path.join(img_dir, c) 
        try:       
            imgs = os.listdir(d)
        except:
            continue
        for i in [f for f in imgs if ('png' in f)]:
            x.append(cv2.imread(os.path.join(d, i), 0))
            y.append(label)            
        label += 1
    return np.array(x)/255, to_categorical(y)

import matplotlib.pyplot as plt
def flip_img(img, Y):
  flip_ = [cv2.flip(i, 1) for i in img]
  return np.array(flip_).reshape(len(X), H, W, 1), Y

# train dataset
X, Y = make_train_dataset('img')
H = X.shape[1]
W = X.shape[2]
X = np.reshape(X, (len(X), H, W, 1))
print(len(X), len(Y), X.shape, Y.shape)

# valid dataset
valid_X, valid_y = flip_img(X, Y)
print(valid_X.shape, valid_y[3])

# callback
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3, verbose=1)
callback = [reduce_lr]

# config
batch_size = 10
num_ep = 20
inputs = Input((H, W, 1))
model = create_model(inputs)
model.summary()

try:
    model.fit(X, Y, batch_size=batch_size, epochs=num_ep, callbacks=callback,
                          validation_data=(valid_X, valid_y), shuffle=True)
finally:
    model.save('../SecurityCamera/CNN_model.h5')

