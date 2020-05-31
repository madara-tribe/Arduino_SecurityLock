# -*- coding: utf-8 -*-
import numpy as np
import os
import cv2
import keras
from keras.models import Model
from keras.layers import *
from train_modules.scse import channel_spatial_squeeze_excite
import serial
import time

def create_model(inputs_):
  o = Conv2D(32, (3, 3), padding='same', kernel_initializer='random_uniform')(inputs_)
  o = channel_spatial_squeeze_excite(o)
  o = MaxPooling2D((2, 2))(o)
  o = Conv2D(64, (3, 3), padding='same', kernel_initializer='random_uniform')(o)
  o = channel_spatial_squeeze_excite(o)
  o = MaxPooling2D((2, 2))(o)
  o = Conv2D(64, (3, 3), padding='same', kernel_initializer='random_uniform')(o)
  o = channel_spatial_squeeze_excite(o)
  o = Flatten()(o)
  o = Dense(6, activation='softmax')(o)
  model = Model(inputs=inputs_, outputs=o)
  model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
  return model       


H = 256
W = 256
inputs = Input((H, W, 1))
model = create_model(inputs)
model.load_weights('train_modules/CNN_model.h5')
key_file = 'SecurityCamera/key.txt'
cap = cv2.VideoCapture(0)

with serial.Serial('/dev/cu.usbmodem14301', timeout=0.1) as ser:

    while True:
        ret, frame = cap.read()            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        xp = int(frame.shape[1]/2)
        yp = int(frame.shape[0]/2)
        d = 400 # bbox size
        resize = 256
        cv2.rectangle(gray, (xp-d, yp-d), (xp+d, yp+d), color=0, thickness=10)
        cv2.imshow('gray', gray)
        if cv2.waitKey(10) == 27:
            break
        a = ser.read()
        print(a)
        if a == b'1':
            print('pass')
            gray = cv2.resize(gray[yp-d:yp + d, xp-d:xp + d],(resize, resize))
            img = np.asarray(gray,dtype=np.float32)  
            img = np.reshape(img, (1, 256, 256, 1))
            img = img/255
            y_pred = model.predict(img)
            c = int(np.argmax(y_pred, axis=1))
            print(c)
            with open('key.txt', 'r') as f:
                b = int(f.read())
            if b==0:
                if c!=0:
                    time.sleep(5.0) # wait 5 second
                    ser.write(b"o")
                    with open(key_file, 'w') as f:
                        f.write(str(c))
                    print('close')
            else:
                if b==c:
                    time.sleep(5.0) # wait 5 second
                    ser.write(b"c")
                    with open(key_file, 'w') as f:
                        f.write('0')
                    print('open')
cap.release()